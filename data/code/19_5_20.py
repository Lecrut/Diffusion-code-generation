def run_length_encode(input_string, max_run_length=5):
    if not input_string:
        return []
    
    encoded = []
    i = 0
    n = len(input_string)
    
    while i < n:
        char = input_string[i]
        run_length = 0
        
        while i < n and run_length < max_run_length:
            if input_string[i] == char:
                run_length += 1
                i += 1
            else:
                break
        
        encoded.append((char, run_length))
        
    return encoded

def run_length_decode(encoded_list):
    decoded_parts = []
    
    for char, count in encoded_list:
        decoded_parts.append(char * count)
        
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_string = "AAAAABBBCCDAA"
    max_run = 4
    encoded = run_length_encode(sample_string, max_run)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)