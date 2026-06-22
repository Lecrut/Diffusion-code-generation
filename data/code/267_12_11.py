MAX_WORD_LENGTH = 6

def is_any_word_longer_than_max(words):
    return any(len(word) > MAX_WORD_LENGTH for word in words.split())

if __name__ == '__main__':
    print(is_any_word_longer_than_max("hello world"))
    print(is_any_word_longer_than_max("hi there"))
    print(is_any_word_longer_than_max("programming is fun"))