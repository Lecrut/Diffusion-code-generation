def check_same_chars(phrase1, phrase2):
    return set(phrase1) == set(phrase2)
if __name__ == '__main__':
    print(check_same_chars('listen', 'silent'))
    print(check_same_chars('hello', 'world'))