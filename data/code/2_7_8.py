def is_palindrome(s):
    return all(a == b for a, b in zip(s, reversed(s)))

if __name__ == '__main__':
    sample1 = "racecar"
    sample2 = "hello"
    sample3 = "noon"
    print(is_palindrome(sample1))
    print(is_palindrome(sample2))
    print(is_palindrome(sample3))