def normalize_alphanumeric(text):
    result = []
    for char in text:
        if char.isalnum():
            result.append(char.lower())
    return "".join(result)

def is_palindrome(text):
    cleaned = normalize_alphanumeric(text)
    length = len(cleaned)
    if length == 0:
        return True
    middle = length // 2
    for index in range(middle):
        if cleaned[index] != cleaned[length - 1 - index]:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "Mr. Owl ate my metal worm",
        "Step on no pets",
        "The quick brown fox jumps over the lazy dog",
        "12321",
        "Not a palindrome",
        "Able was I, ere I saw Elba"
    ]
    for sample in test_cases:
        print(is_palindrome(sample))