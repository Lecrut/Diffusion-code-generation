def normalize_text(text):
    return text.lower().replace(" ", "")

def reverse_string(text):
    return text[::-1]

def check_palindrome_raw(text):
    normalized = normalize_text(text)
    return normalized == reverse_string(normalized)

if __name__ == '__main__':
    test_inputs = ["radar", "level", "python", "step on no pets", "hello world"]
    for sample in test_inputs:
        result = check_palindrome_raw(sample)
        print(result)