def validate_input(phrase1: str, phrase2: str) -> None:
    if not isinstance(phrase1, str) or not isinstance(phrase2, str):
        raise ValueError("Both inputs must be strings")

def check_same_characters(phrase1: str, phrase2: str) -> bool:
    validate_input(phrase1, phrase2)
    return set(phrase1) == set(phrase2)

if __name__ == '__main__':
    print(check_same_characters("listen", "silent"))
    print(check_same_characters("hello", "world"))
    print(check_same_characters("binary", "brainy"))
    print(check_same_characters("apple", "papel"))
    print(check_same_characters("rat", "car"))