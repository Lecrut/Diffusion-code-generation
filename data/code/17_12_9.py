def run_length_encode(input_string):
    if not input_string:
        return {}
    
    result = {}
    i = 0
    n = len(input_string)
    
    while i < n:
        char = input_string[i]
        if not char.isalnum():
            i += 1
            continue
        
        count = 0
        while i < n and input_string[i] == char:
            count += 1
            i += 1
        
        result[char] = count
    
    return result

if __name__ == '__main__':
    sample = "aAa11bb22cc"
    encoded = run_length_encode(sample)
    print(encoded)