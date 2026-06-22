def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_inputs = ["Racecar", "hello", "A man a plan a canal Panama", "Python"]
    for sample in sample_inputs:
        result = is_palindrome(sample)
        print(result)