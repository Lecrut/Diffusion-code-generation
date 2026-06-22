def any_word_longer_than(s, length=6):
    return any(len(word) > length for word in s.split())

if __name__ == '__main__':
    print(f"String 'hello world': {any_word_longer_than('hello world')}")
    print(f"String 'short words only': {any_word_longer_than('short words only')}")
    print(f"String 'one very long word indeed': {any_word_longer_than('one very long word indeed')}")