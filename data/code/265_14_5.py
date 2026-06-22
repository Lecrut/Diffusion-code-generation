def check_same_characters(phrase1: str, phrase2: str) -> bool:
    return set(phrase1) == set(phrase2)
if __name__ == '__main__':
    print(check_same_characters('listen', 'silent'))
    print(check_same_characters('hello', 'world'))