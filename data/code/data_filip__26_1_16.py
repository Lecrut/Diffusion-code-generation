def run_length_encode(data):
    if not data:
        return ""
    
    result = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(data[i - 1] + str(count))
            count = 1
    
    result.append(data[length - 1] + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    sample_input2 = "AABCCC"
    encoded_result2 = run_length_encode(sample_input2)
    print(encoded_result2)
    
    empty_input = ""
    encoded_empty = run_length_encode(empty_input)
    print(encoded_empty)