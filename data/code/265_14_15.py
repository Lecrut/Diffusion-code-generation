def check_same_characters(phrase1: str, phrase2: str) -> bool:
    try:
        return set(phrase1.lower()) == set(phrase2.lower())
    except TypeError as e:
        raise ValueError("Input must be strings") from e

if __name__ == '__main__':
    print(check_same_characters("listen", "silent"))
    print(check_same_characters("hello", "world"))
    print(check_same_characters("binary", "brainy"))
    print(check_same_characters("apple", "papel"))
    print(check_same_characters("rat", "car"))