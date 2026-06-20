def check_palindrome(text):
    filtered = []
    for char in text:
        if char.isalnum():
            filtered.append(char.lower())
    left = 0
    right = len(filtered) - 1
    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    samples = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon"
    ]
    for sample in samples:
        print(check_palindrome(sample))