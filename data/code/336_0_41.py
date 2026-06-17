import sys
def check_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = ["Hello", "PythonScript", "abcdef"]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"String '{s}': {'Repeated characters found.' if result else 'No repeated characters.'}")