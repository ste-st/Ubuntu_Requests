import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    # Prompt the user for the image URL
    url = input("Enter the image URL: ").strip()
    
    # Create the directory if it doesn't exist
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)
    
    try:
        # Fetch the image from the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            # Generate a unique filename if none is provided
            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

        # Full path to save the image
        file_path = os.path.join(folder_name, filename)

        # Save the image in binary mode
        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Could not fetch the image. Reason: {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
