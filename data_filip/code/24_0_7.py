def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    count = 1
    length = len(input_string)
    previous_char = input_string[0]
    
    for i in range(1, length):
        current_char = input_string[i]
        if current_char == previous_char:
            count += 1
        else:
            result.append(previous_char)
            if count > 1:
                result.append(str(count))
            previous_char = current_char
            count = 1
    
    result.append(previous_char)
    if count > 1:
        result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccd"
    compressed = run_length_encode(sample_input)
    print(compressed)