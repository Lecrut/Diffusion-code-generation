def is_palindrome(text: str) -> bool:
    return text == text[::-1]

if __name__ == '__main__':
    sample_text = "racecar"
    result = is_palindrome(sample_text)
    print(result)
    sample_text2 = "hello"
    result2 = is_palindrome(sample_text2)
    print(result2)