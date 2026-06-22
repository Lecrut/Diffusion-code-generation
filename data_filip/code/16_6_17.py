def run_length_encode(strings: list[str]) -> list[tuple]:
    if not strings:
        return []
    
    result = []
    current_string = strings[0]
    current_count = 1
    
    for i in range(1, len(strings)):
        if strings[i] == current_string:
            current_count += 1
        else:
            result.append((current_string, current_count))
            current_string = strings[i]
            current_count = 1
            
    result.append((current_string, current_count))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd']
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)