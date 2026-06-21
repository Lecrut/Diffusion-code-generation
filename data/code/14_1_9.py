def has_unique_characters(s):
    if len(s) > 128:
        return False
    
    checker = 0
    
    for char in s:
        val = ord(char)
        
        if (checker & (1 << val)) > 0:
            return False
        
        checker |= (1 << val)
    
    return True

if __name__ == '__main__':
    test_string = "abcde"
    result = has_unique_characters(test_string)
    print(result)