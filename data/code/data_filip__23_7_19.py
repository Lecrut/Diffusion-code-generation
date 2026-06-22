def rle_encode(data):
    if not data:
        return ""
    
    result = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(data[i - 1])
            count = 1
    
    result.append(str(count))
    result.append(data[-1])
    
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccdddd"
    encoded_output = rle_encode(sample_input)
    print(encoded_output)
    
    sample_input_2 = "A"
    encoded_output_2 = rle_encode(sample_input_2)
    print(encoded_output_2)
    
    sample_input_3 = "AABBCCDDEE"
    encoded_output_3 = rle_encode(sample_input_3)
    print(encoded_output_3)