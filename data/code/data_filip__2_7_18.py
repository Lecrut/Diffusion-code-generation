def check_palindrome(s):
    return all(a == b for a, b in zip(s, reversed(s)))

if __name__ == '__main__':
    sample_string = "radar"
    result = check_palindrome(sample_string)
    print(result)