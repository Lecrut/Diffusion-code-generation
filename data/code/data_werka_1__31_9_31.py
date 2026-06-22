def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ["racecar", "hello", "level", "world", "madam"]
    results = {value: is_palindrome(value) for value in sample_values}
    print(results)