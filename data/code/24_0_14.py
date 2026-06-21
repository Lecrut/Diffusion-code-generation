def compress(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = input_string[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccdde"
    compressed_output = compress(sample_input)
    print(compressed_output)