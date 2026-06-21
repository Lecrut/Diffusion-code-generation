def run_length_encode(strings):
    if not strings:
        return []
    
    encoded = []
    current_string = strings[0]
    count = 1
    
    for i in range(1, len(strings)):
        if strings[i] == current_string:
            count += 1
        else:
            encoded.append((count, current_string))
            current_string = strings[i]
            count = 1
    
    encoded.append((count, current_string))
    return encoded

if __name__ == '__main__':
    sample_list = ["a", "a", "b", "b", "b", "c", "a", "a", "a", "a"]
    result = run_length_encode(sample_list)
    print(result)