def is_palindrome(s):
    LEFT_INDEX = 0
    RIGHT_INDEX = len(s) - 1
    
    while LEFT_INDEX < RIGHT_INDEX:
        if s[LEFT_INDEX] != s[RIGHT_INDEX]:
            return False
        LEFT_INDEX += 1
        RIGHT_INDEX -= 1
    
    return True

if __name__ == '__main__':
    SAMPLE_VALUES = ["racecar", "hello", "madam", "python", "level", "world"]
    for value in SAMPLE_VALUES:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")