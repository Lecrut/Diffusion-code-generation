def is_long(word):
    return len(word) > 8

if __name__ == '__main__':
    words = ["apple", "pineapple", "kiwi", "orange"]
    for word in words:
        print(f"The word '{word}' is long: {is_long(word)}")