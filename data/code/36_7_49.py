def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def is_valid_unicode(char):
        return ord(char) < 0x110000
    
    if any(not is_valid_unicode(char) for char in s):
        raise ValueError("String contains invalid Unicode characters")
    
    reversed_chars = []
    for char in s:
        reversed_chars.insert(0, char)
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)