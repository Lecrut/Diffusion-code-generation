def is_palindrome_check(s): return s == ''.join(reversed(s))

if __name__ == '__main__': 
    print(is_palindrome_check("racecar"))