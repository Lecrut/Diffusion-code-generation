import string

def contains_special_characters(s: str) -> bool:
    stripped = ''.join(char for char in s if char not in string.punctuation and char.isspace())
    return len(stripped) != len(s)

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "Hello, World!",
        "NoSpecialChars123",
        "@#$$%",
        "Mix 123 !@#",
        "",
        "   ",
        "Just letters abc",
        "Special @ symbols & chars !"
    ]
    results = [contains_special_characters(s) for s in test_cases]
    for s, res in zip(test_cases, results):
        print(f"{repr(s)}: {res}")