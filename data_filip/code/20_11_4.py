def run_length_encode(numeric_string):
    if not numeric_string:
        return []
    
    encoded = []
    current_char = numeric_string[0]
    count = 1
    
    for i in range(1, len(numeric_string)):
        if numeric_string[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = numeric_string[i]
            count = 1
    
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_string = "11122112222"
    result = run_length_encode(sample_string)
    print(result)