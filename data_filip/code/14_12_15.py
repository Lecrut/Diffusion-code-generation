def has_duplicate_chars(s: str) -> bool:
    if not s:
        return False
    
    bitmask = 0
    for char in s:
        if not ('a' <= char <= 'z'):
            continue
        
        index = ord(char) - ord('a')
        mask = 1 << index
        
        if bitmask & mask:
            return True
        
        bitmask |= mask
        
    return False

if __name__ == '__main__':
    sample_strings = [
        "abcde",
        "hello",
        "python",
        "aabbcc",
        "abcdefghijklmnopqrstuvwxyz"
    ]
    
    for s in sample_strings:
        result = has_duplicate_chars(s)
        print(result)