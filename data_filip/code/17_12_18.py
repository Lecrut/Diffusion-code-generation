def run_length_encode(s):
    if not s:
        return {}
    
    result = {}
    count = 0
    current_char = s[0]
    
    for char in s:
        if char.isalnum():
            if char == current_char:
                count += 1
            else:
                if current_char in result:
                    result[current_char] += count
                else:
                    result[current_char] = count
                current_char = char
                count = 1
        else:
            if current_char in result:
                result[current_char] += count
            else:
                result[current_char] = count
            current_char = char
            count = 1
    
    if current_char in result:
        result[current_char] += count
    else:
        result[current_char] = count
        
    sorted_keys = sorted(result.keys())
    ordered_result = {}
    for key in sorted_keys:
        ordered_result[key] = result[key]
        
    return ordered_result

if __name__ == '__main__':
    sample_string = "AABBCCCDD"
    encoded = run_length_encode(sample_string)
    print(encoded)