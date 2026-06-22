def compress_string(input_str):
    if not input_str:
        return ""
    
    result = []
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            result.append(f"{input_str[i-1]}{count}")
            count = 1
    result.append(f"{input_str[-1]}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabbcc"
    compressed_output = compress_string(sample_input)
    print(compressed_output)