def validate_input(phrase1, phrase2):
    if not isinstance(phrase1, str) or not isinstance(phrase2, str):
        raise ValueError("Both inputs must be strings")
    if not phrase1 and not phrase2:
        return False
    return True

def have_same_characters(phrase1: str, phrase2: str) -> bool:
    if not validate_input(phrase1, phrase2):
        return False
    return set(phrase1) == set(phrase2)

if __name__ == '__main__':
    print(have_same_characters("listen", "silent"))
    print(have_same_characters("hello", "world"))
    print(have_same_characters("binary", "brainy"))
    print(have_same_characters("apple", "papel"))
    print(have_same_characters("rat", "car"))