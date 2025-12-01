import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def play_music(folder, mp3_files, current_index ):
    while(True):
        song_name = mp3_files[current_index]
        file_path = os.path.join(folder, song_name)
        if not os.path.exists(file_path):
            print("File not found")
            return
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        print(f"\n Now Playing: {song_name}")
        print("Commands: [P]ause, [R]esume, [S]top, [N]ext")
        is_running = True
        while(is_running):

            command = input("> ").upper()

            if command == "P":
                pygame.mixer.music.pause()
                print("Paused")
            elif  command == "R":
                pygame.mixer.music.unpause()
                print("Resumed")
            elif command == "S":
                pygame.mixer.music.stop()
                print("Stopped")
                return
            elif command == "N":
                print("Playing next")
                pygame.mixer.music.stop()
                current_index = (current_index + 1) % len(mp3_files)
                is_running = False
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
            else:
                print("INVALID INPUT")

    
def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initiallisation failed!",e)
        return  
    folder = "music"

    if not os.path.isdir(folder):
        print(f"folder '{folder}' not found!!")
        return 

    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")] 
    if not mp3_files:
        print("No .mp3 files found!!")

    while(True):
        print("******MP3 PLAYER******")
        print("MY song list:")
        for index, song in enumerate(mp3_files, start=1 ):
            print(f"{index}.{song}") 
        choice_input = input("\n Enter the song # to play (or Q to quit)\n").upper()
        if choice_input == "Q":
            print("Bye!")
            break
        if not choice_input.isdigit():
            print("Enter a valid number")
            continue
        choice = int(choice_input) - 1
        if 0<= choice <len(mp3_files):
            play_music(folder,mp3_files, choice )
        else:
            print("INVALID CHOICE!!")                       


if __name__ == "__main__":
    main()