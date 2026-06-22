def normalize_text(text):
    return ''.join(char for char in text if char.isalnum()).lower()

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    normalized = normalize_text(text)
    return normalized == reverse_string(normalized)

if __name__ == '__main__':
    test_inputs = [
        "Step on no pets",
        "Not a palindrome",
        "12321",
        "No 'x' in Nixon",
        "Python"
    ]
    for sample in test_inputs:
        print(is_palindrome(sample))