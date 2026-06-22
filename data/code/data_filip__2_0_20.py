def is_palindrome(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    sample_string_1 = "radar"
    sample_string_2 = "hello"
    result_1 = is_palindrome(sample_string_1)
    result_2 = is_palindrome(sample_string_2)
    print(result_1)
    print(result_2)