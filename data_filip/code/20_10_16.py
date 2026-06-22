def rle_encode(input_string: str) -> str:
    if not input_string:
        return ""

    result = []
    current_char = input_string[0]
    count = 1
    length = len(input_string)

    for i in range(1, length):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbc"
    encoded_output = rle_encode(sample_string)
    print(encoded_output)