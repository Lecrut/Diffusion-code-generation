def is_palindrome(s):
    return all(c == d for c, d in zip(s, s[::-1]))

if __name__ == '__main__':
    result = is_palindrome("racecar")
    print(result)