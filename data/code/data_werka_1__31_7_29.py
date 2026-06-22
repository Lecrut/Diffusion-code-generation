def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "No 'x' in Nixon"
    ]
    
    for value in sample_values:
        print(is_palindrome(value))