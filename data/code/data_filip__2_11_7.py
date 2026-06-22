def reverse_string(text: str) -> str:
    length = len(text)
    reversed_chars = []
    index = length - 1
    while index >= 0:
        reversed_chars.append(text[index])
        index -= 1
    return ''.join(reversed_chars)

def is_palindrome(text: str) -> bool:
    original = text
    reversed_text = reverse_string(original)
    return original == reversed_text

if __name__ == '__main__':
    sample_cases = [
        "level",
        "world",
        "noon",
        "Python",
        "madam",
        "code"
    ]
    for sample in sample_cases:
        result = is_palindrome(sample)
        print(result)