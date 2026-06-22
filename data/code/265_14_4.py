def check_same_characters(phrase1, phrase2):
    return set(phrase1) == set(phrase2)
if __name__ == '__main__':
    print(check_same_characters('listen', 'silent'))
    print(check_same_characters('hello', 'world'))