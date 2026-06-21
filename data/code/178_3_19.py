if __name__ == '__main__':
    phrase = "Hello,world!,,How are you?,everyone?"
    words = [word.strip(',!?') for word in phrase.split(',') if word]
    print(words)