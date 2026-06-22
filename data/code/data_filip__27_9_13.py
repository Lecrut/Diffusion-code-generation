def run_length_encode(input_string):
    if not input_string:
        return []
    
    result = []
    current_char = input_string[0]
    count = 0
    
    for char in input_string:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
            
    result.append((current_char, count))
    
    return result

if __name__ == '__main__':
    encoded = run_length_encode('aabbaaccc')
    print(encoded)