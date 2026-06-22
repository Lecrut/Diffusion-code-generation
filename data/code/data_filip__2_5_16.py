def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    samples = ["Racecar", "Hello", "A man a plan a canal Panama", "No 'x' in Nixon", "Python"]
    for sample in samples:
        result = is_palindrome(sample)
        print(result)