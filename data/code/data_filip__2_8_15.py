def normalize_text(text):
    result = []
    for char in text:
        if char.isalnum():
            result.append(char.lower())
    return "".join(result)

def check_palindrome(input_string):
    normalized = normalize_text(input_string)
    length = len(normalized)
    mid = length // 2
    for index in range(mid):
        if normalized[index] != normalized[length - 1 - index]:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "Able was I, ere I saw Elba!",
        "Not a palindrome",
        "Madam",
        "12321",
        "No 'x' in Nixon"
    ]
    for item in test_cases:
        print(check_palindrome(item))