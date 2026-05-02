def is_palindrome_memory_efficient(s):
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
    print(f"'{string1}': {is_palindrome_memory_efficient(string1)}")
    print(f"'{string2}': {is_palindrome_memory_efficient(string2)}")
    print(f"'{string3}': {is_palindrome_memory_efficient(string3)}")
    print(f"'{string4}': {is_palindrome_memory_efficient(string4)}")