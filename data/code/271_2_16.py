def is_palindrome(s):
    filtered_chars = [char.lower() for char in s if char.isalpha()]
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    sample_string = "No 'x' in Nixon"
    result = is_palindrome(sample_string)
    print(result)