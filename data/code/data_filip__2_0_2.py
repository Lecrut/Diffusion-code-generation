def check_palindrome(text):
    normalized = text.lower()
    start = 0
    end = len(normalized) - 1
    while start < end:
        if normalized[start] != normalized[end]:
            return False
        start += 1
        end -= 1
    return True

if __name__ == '__main__':
    samples = [
        "Racecar",
        "Hello",
        "A Santa At NASA",
        "No lemon, no melon",
        "Python",
        "Madam"
    ]
    for sample in samples:
        result = check_palindrome(sample)
        print(result)