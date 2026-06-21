def has_vowels(word):
    vowels = 2863311530
    return any((vowels & 1 << ord(c.lower()) - ord('a') != 0 for c in word))
if __name__ == '__main__':
    words = ['hello', 'world', 'Python', 'bitwise']
    print([word for word in words if has_vowels(word)])