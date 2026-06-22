def normalize_text(raw):
    buffer = []
    for char in raw:
        if char.isalnum():
            buffer.append(char.lower())
    return "".join(buffer)

def check_palindrome(raw):
    cleaned = normalize_text(raw)
    length = len(cleaned)
    mid = length // 2
    for index in range(mid):
        if cleaned[index] != cleaned[length - 1 - index]:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "No lemon, no melon",
        "Step on no pets",
        "The quick brown fox",
        "12321",
        "12345",
        "Was it a car or a cat I saw?",
        "Madam"
    ]
    for item in test_cases:
        result = check_palindrome(item)
        print(result)