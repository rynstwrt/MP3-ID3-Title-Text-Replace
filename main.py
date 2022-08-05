from glob import glob
from mutagen.mp3 import EasyMP3
from os import path, access, W_OK
from console_colors import ConsoleColors


def print_all_id3_title_tags(dir):
    mp3_files = glob(u'%s\\*.mp3' % dir)
    for mp3_file_path in mp3_files:
        audio = EasyMP3(mp3_file_path)
        print(audio.tags["title"][0])


def replace_text_in_id3_titles(dir, target, replacement):
    mp3_files = glob(u'%s\\*.mp3' % dir)
    for index, mp3_file_path in enumerate(mp3_files):
        audio = EasyMP3(mp3_file_path)

        title = audio.tags["title"][0]

        if target in title:
            new_title = audio.tags["title"][0].replace(target, replacement)
            print("%d REPLACING '%s' WITH '%s'" % (index, title, new_title))
            audio.tags["title"] = new_title
            audio.save()

    print("")
    print("SUCCESSFULLY REPLACED TEXT IN THE MP3 FILES' ID3 TITLE.")


if __name__ == "__main__":
    print("")
    print(ConsoleColors.OKCYAN + ConsoleColors.UNDERLINE + "SELECT WHAT YOU WANT TO DO:" + ConsoleColors.ENDC)
    print("1. READ ALL THE ID3 TITLES OF MP3S IN A DIRECTORY.")
    print("2. REPLACE TEXT IN ID3 TITLES OF MP3S IN A DIRECTORY.")
    print("3. EXIT.")
    print("")
    choice = input("ENTER 1, 2, or 3: ")

    print("")

    if choice == "3":
        exit()

    directory = input("ENTER THE PATH TO THE DIRECTORY THAT HOLDS THE MP3 FILES: ")
    if not path.exists(directory) or not access(path.dirname(directory), W_OK):
        raise NotADirectoryError('"%s" IS NOT A VALID PATH TO A DIRECTORY.' % directory)

    print("")

    if choice == "1":
        header_text = "HERE ARE ALL THE ID3 TITLE TAGS IN %s:" % directory
        print(header_text)
        print("-" * len(header_text))
        print_all_id3_title_tags(directory)

    elif choice == "2":
        target_string = input("ENTER THE TEXT YOU WANT TO REPLACE: ")
        print("")
        replacement_string = input('ENTER THE TEXT YOU WANT TO REPLACE "%s" WITH: ' % target_string)
        print("")
        replace_text_in_id3_titles(directory, target_string, replacement_string)

    else:
        raise ValueError('"%s" IS NOT A VALID OPTION.' % choice)
