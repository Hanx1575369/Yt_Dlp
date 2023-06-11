import yt_dlp

def download_audio(link):
    try:
        with yt_dlp.YoutubeDL({'format': 'bestaudio', 'outtmpl': 'audio/%(title)s.mp3', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}]}) as video:
            info_dict = video.extract_info(link, download=True)
            video_title = info_dict['title']
            print(video_title)
    except Exception as e:
        print(f"An error occurred: {e}")

with open('list.txt', 'r') as f:
    links = set(f.read().split(','))
for i in links:
    download_audio(i)