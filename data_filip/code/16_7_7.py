def run_length_encode(binary_string):
    if not binary_string:
        return []
    
    result = []
    current_char = binary_string[0]
    count = 1
    
    for i in range(1, len(binary_string)):
        if binary_string[i] == current_char:
            count += 1
        else:
            result.append(count)
            current_char = binary_string[i]
            count = 1
    result.append(count)
    return result

if __name__ == '__main__':
    binary_str = '111000001111'
    encoded = run_length_encode(binary_str)
    print(encoded)