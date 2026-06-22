def compress_rle(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for index in range(1, len(input_string)):
        if input_string[index] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = input_string[index]
            count = 1
    
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccddee"
    compressed_output = compress_rle(sample_input)
    print(compressed_output)