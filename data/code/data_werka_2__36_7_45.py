def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def is_valid_unicode_char(c):
        try:
            c.encode('utf-8')
            return True
        except UnicodeEncodeError:
            return False
    
    for char in s:
        if not is_valid_unicode_char(char):
            raise ValueError(f"Invalid Unicode character: {char}")
    
    reversed_chars = [s[i] for i in range(len(s) - 1, -1, -1)]
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)