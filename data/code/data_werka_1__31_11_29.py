def is_palindrome_two_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_slicing(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    sample_values = ["racecar", "hello", "level", "world", "madam"]
    
    for value in sample_values:
        print(f"Two-pointers approach: {value} is a palindrome - {is_palindrome_two_pointers(value)}")
        print(f"Slicing approach: {value} is a palindrome - {is_palindrome_slicing(value)}")