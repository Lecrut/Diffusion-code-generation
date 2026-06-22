def run_length_encode(strings):
    if not strings:
        return []
    
    result = []
    current_string = strings[0]
    count = 1
    
    for i in range(1, len(strings)):
        if strings[i] == current_string:
            count += 1
        else:
            result.append((current_string, count))
            current_string = strings[i]
            count = 1
    
    result.append((current_string, count))
    return result

if __name__ == '__main__':
    sample_strings = ['A', 'A', 'A', 'B', 'B', 'C', 'A', 'A', 'A', 'A']
    encoded = run_length_encode(sample_strings)
    print(encoded)