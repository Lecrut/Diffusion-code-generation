def run_length_encode(input_string):
    if not input_string:
        return ""
    
    iterator = iter(input_string)
    try:
        current_char = next(iterator)
    except StopIteration:
        return ""
    
    count = 1
    result = []
    
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAABBB"
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)