def run_length_encode(binary_string):
    if not binary_string:
        return []
    
    result = []
    current_count = 1
    
    for i in range(1, len(binary_string)):
        if binary_string[i] == binary_string[i - 1]:
            current_count += 1
        else:
            result.append(current_count)
            current_count = 1
    
    result.append(current_count)
    return result

if __name__ == '__main__':
    sample = "1110011110001"
    print(run_length_encode(sample))