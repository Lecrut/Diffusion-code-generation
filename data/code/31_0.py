def is_palindrome(s):
    processed_s = "".join(filter(str.isalnum, s)).lower()
    return processed_s == processed_s[::-1]
if __name__ == '__main__':
    print(f"Test 'racecar': {is_palindrome('racecar')}")
    print(f"Test 'A man, a plan, a canal: Panama': {is_palindrome('A man, a plan, a canal: Panama')}")
    print(f"Test 'hello': {is_palindrome('hello')}")
    print(f"Test 'Madam': {is_palindrome('Madam')}")
    print(f"Test '121': {is_palindrome('121')}")
    print(f"Test 'No lemon, no melon': {is_palindrome('No lemon, no melon')}")
    print(f"Test 'abcde': {is_palindrome('abcde')}")