def encode_rle(input_string):
    if not input_string:
        return ""
    
    result = []
    count = 1
    length = len(input_string)
    
    for i in range(1, length):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(input_string[i - 1])
            count = 1
    
    result.append(str(count))
    result.append(input_string[-1])
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    encoded_value = encode_rle(sample_input)
    print(encoded_value)