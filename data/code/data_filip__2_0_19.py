def is_palindrome(text):
    start = 0
    end = len(text) - 1
    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True

if __name__ == '__main__':
    sample_string_1 = "radar"
    sample_string_2 = "hello"
    sample_string_3 = "A man a plan a canal Panama"
    print(is_palindrome(sample_string_1))
    print(is_palindrome(sample_string_2))
    print(is_palindrome(sample_string_3))