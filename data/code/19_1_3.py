def decode_rle(encoded_string):
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    n = len(encoded_string)
    
    while i < n:
        if not encoded_string[i].isdigit():
            raise ValueError(f"Invalid input format: expected digit at index {i}, got '{encoded_string[i]}'")
        
        count_start = i
        while i < n and encoded_string[i].isdigit():
            i += 1
        
        count = int(encoded_string[count_start:i])
        
        if i >= n:
            raise ValueError("Invalid input format: missing character after count")
        
        char = encoded_string[i]
        i += 1
        
        if count < 0:
            raise ValueError("Invalid input format: negative count")
            
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "12A3B2C",
        "5X10Y1Z",
        "1A2B3C4D5E",
        "100A",
        "2A2B"
    ]
    
    for test_input in test_cases:
        try:
            decoded = decode_rle(test_input)
            print(decoded)
        except ValueError as e:
            print(f"Error: {e}")
    
    invalid_case = "A12B"
    try:
        decode_rle(invalid_case)
    except ValueError as e:
        print(f"Error: {e}")