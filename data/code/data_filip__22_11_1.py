def run_length_decode(encoded: str) -> str:
    decoded = []
    num_str = []
    
    for char in encoded:
        if char.isdigit():
            num_str.append(char)
        else:
            if num_str:
                count = int(''.join(num_str))
                decoded.append(char * count)
                num_str = []
            else:
                decoded.append(char)
                
    if num_str:
        count = int(''.join(num_str))
        if decoded:
            last_char = decoded.pop()
            decoded.append(last_char * count)
        else:
            decoded.append(last_char * count)
            
    return ''.join(decoded)

def run_length_decode_empty(encoded: str) -> str:
    return run_length_decode(encoded)

if __name__ == '__main__':
    encoded_string = "a3b2c1"
    result = run_length_decode(encoded_string)
    print(result)
    
    encoded_empty = ""
    result_empty = run_length_decode_empty(encoded_empty)
    print(result_empty)
    
    encoded_single = "z10"
    result_single = run_length_decode(encoded_single)
    print(result_single)
    
    encoded_mixed = "a1b1c1d1"
    result_mixed = run_length_decode(encoded_mixed)
    print(result_mixed)