import pydub, spotipy

def info_Spotify():
    spotfy = Spotipy.Spotify()
    result = spotfy.search(q = "Centuries", limit = 10)
    return result

print info_Spotify()
