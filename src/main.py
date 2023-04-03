from plus import usage1
import cloudmusic

if __name__ == '__main__':
    playlist = cloudmusic.getPlaylist(8134828337)
    for music in playlist:
        usage1.download(music)
