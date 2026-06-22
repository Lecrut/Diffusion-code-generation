def have_same_characters(phrase1: str, phrase2: str) -> bool:
    return set(phrase1) == set(phrase2)

if __name__ == '__main__':
    print(have_same_characters("listen", "silent"))
    print(have_same_characters("hello", "world"))
    print(have_same_characters("binary", "brainy"))
    print(have_same_characters("apple", "papel"))
    print(have_same_characters("rat", "car"))