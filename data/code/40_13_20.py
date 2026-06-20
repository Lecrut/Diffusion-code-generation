def extract_first_alpha(s: str) -> str:
    for char in s:
        if char.isalpha():
            return char
    return ""

if __name__ == "__main__":
    test_strings = ["123abc", "!@#Test", "   ", "Alpha", "99Zebra"]
    for text in test_strings:
        result = extract_first_alpha(text)
        print(f"Input: '{text}' -> First Alpha: '{result}'")