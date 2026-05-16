def is_palindrome_optimized(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True
if __name__ == '__main__':
    string1 = "racecar"
    string2 = "hello"
    string3 = "madam"
    string4 = "world"
    string5 = "aabbaa"
    print(f"'{string1}' is palindrome: {is_palindrome_optimized(string1)}")
    print(f"'{string2}' is palindrome: {is_palindrome_optimized(string2)}")
    print(f"'{string3}' is palindrome: {is_palindrome_optimized(string3)}")
    print(f"'{string4}' is palindrome: {is_palindrome_optimized(string4)}")
    print(f"'{string5}' is palindrome: {is_palindrome_optimized(string5)}")