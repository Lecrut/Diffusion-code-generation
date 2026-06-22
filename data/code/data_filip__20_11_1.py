def run_length_encode_numeric_string(numeric_string):
    if not numeric_string:
        return []
    
    encoded = []
    current_char = numeric_string[0]
    count = 1
    
    for i in range(1, len(numeric_string)):
        if numeric_string[i] == current_char:
            count += 1
        else:
            encoded.append((int(current_char), count))
            current_char = numeric_string[i]
            count = 1
    
    encoded.append((int(current_char), count))
    return encoded

if __name__ == '__main__':
    sample_string = "112233344445"
    result = run_length_encode_numeric_string(sample_string)
    print(result)