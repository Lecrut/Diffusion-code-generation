def is_palindrome(text):
    reversed_text = text[::-1]
    return text == reversed_text

if __name__ == '__main__':
    sample_one = "radar"
    sample_two = "python"
    sample_three = "refer"
    print(is_palindrome(sample_one))
    print(is_palindrome(sample_two))
    print(is_palindrome(sample_three))