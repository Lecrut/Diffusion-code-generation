def is_palindrome(s):
    char_map = {char.lower(): True for char in 'abcdefghijklmnopqrstuvwxyz'}
    filtered_chars = [char for char in s if char_map.get(char.lower())]
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))