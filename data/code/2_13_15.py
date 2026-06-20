def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = [
        "racecar",
        "hello",
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "no palindrome here",
        "12321",
        ""
    ]
    for sample in samples:
        result = is_palindrome(sample)
        print(result)