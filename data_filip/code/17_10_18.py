def run_length_encode(input_string):
    if not input_string:
        return []
    
    result = []
    iterator = iter(input_string)
    current_char = next(iterator)
    count = 1
    
    for next_char in iterator:
        if next_char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = next_char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "aabcccccaaa"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)