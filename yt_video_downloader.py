from pytube import YouTube


def download_video():
    link = input("Enter the YouTube video link: ")

    try:
        video = YouTube(link)
    except:
        print("\nInvalid YouTube link. Please enter a valid link.")
        return

    print(f"\nTitle: '{video.title}'")
    if video.length is not None:
        print(f"Length: '{video.length // 60} minutes {video.length % 60} seconds'")
    else:
        print("Length: N/A")
    if video.rating is not None:
        print(f"Rating: {video.rating:.2f}/5.00")
    else:
        print("Rating: N/A")
    print(f"Number of views: {video.views}")

    while True:
        try:
            choice = input("\nDo you want to download the video? (Y/N): ")
            if choice.lower() == "y":
                stream = video.streams.get_highest_resolution()
                print(f"\nDownloading '{video.title}'...")
                stream.download()
                print("\nDownload complete.")
                break
            elif choice.lower() == "n":
                print("\nDownload cancelled.")
                break
            else:
                print("\nInvalid input. Please enter Y or N.")
        except:
            print("\nAn error occurred. Download failed.")
            break

download_video()

#the summarize--
"""
from pytube import YouTube

link = input("Enter video link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()

stream.download()
"""