def has_vowels(word):
    vowels = 2863311530
    return any((vowels & 1 << ord(c) - ord('a') for c in word if 'a' <= c <= 'z'))
if __name__ == '__main__':
    words = ['apple', 'banana', 'cherry', 'date']
    print([word for word in words if has_vowels(word)])