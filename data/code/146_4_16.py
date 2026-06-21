def first_non_repeating_char(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None

if __name__ == '__main__':
    print(first_non_repeating_char("swiss"))