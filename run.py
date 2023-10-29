import yt_dlp
import glob
import os


def lobby():
    ask = input('Скачиваем музыку? y/n: ')
    if ask == 'y':
        main()
    else:
        exit()


def main():
    dwn_options = {
# Указываем формат, у меня он другим скачивается, поэтому делаю ренейм
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }

    user_url = input('Вставь ссылку на песню: ')

    try:
        with yt_dlp.YoutubeDL(dwn_options) as ydl:
            ydl.download(user_url)
    except:
        print('Error fmpeg')

# Ренейм по последнему добавленному файлу в МОЕЙ директории
    list_of_files = glob.glob('Z://Dev/linkConverter/*') # Change this path
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    filename = os.path.splitext(latest_file)[0]
    os.rename(latest_file, filename + ".mp3")
    lobby()


# Ну тут бестпрактис... (нет)
if __name__ == '__main__':
    lobby()
