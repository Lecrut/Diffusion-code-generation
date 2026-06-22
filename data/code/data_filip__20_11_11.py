def run_length_encode(numeric_string):
    if not numeric_string:
        return []
    
    encoded = []
    current_char = numeric_string[0]
    count = 1
    
    for char in numeric_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_string = "1122333444445"
    result = run_length_encode(sample_string)
    print(result)