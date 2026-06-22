def decode_rle(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i].isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1
            count = int(s[i:j])
            if j >= n:
                raise ValueError("RLE string ends after count without a character")
            if s[j] == '0':
                raise ValueError("Character cannot be '0' in valid RLE encoding")
            if count <= 0:
                raise ValueError("Count must be positive")
            char = s[j]
            result.append(char * count)
            i = j + 1
        else:
            raise ValueError(f"Invalid character at position {i}: '{s[i]}' is not a digit")
    
    return ''.join(result)

if __name__ == '__main__':
    encoded = "3a4b2c"
    decoded = decode_rle(encoded)
    print(decoded)