def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ["racecar", "hello", "madam", "step on no pets", "notapalindrome"]
    results = {s: is_palindrome(s) for s in sample_values}
    print(results)