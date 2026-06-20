def normalize_string(input_text):
    return ''.join(char.lower() for char in input_text if char.isalnum())

def reverse_text(text):
    return text[::-1]

def is_palindrome(input_text):
    cleaned = normalize_string(input_text)
    return cleaned == reverse_text(cleaned)

if __name__ == '__main__':
    test_cases = [
        "Never odd or even",
        "Hello World",
        "12321",
        "Was it a car or a cat I saw?",
        "Noon",
        "Python"
    ]
    
    for case in test_cases:
        result = is_palindrome(case)
        print(result)