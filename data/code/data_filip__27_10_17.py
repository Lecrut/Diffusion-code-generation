def run_length_encode(data):
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for index in range(1, len(data)):
        if data[index] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = data[index]
            count = 1
    
    encoded.append(str(count) + current_char)
    
    return "".join(encoded)

if __name__ == "__main__":
    sample_string = "AAABBBCCCCDDDDEEEEE"
    result = run_length_encode(sample_string)
    print(result)
    
    empty_string = ""
    empty_result = run_length_encode(empty_string)
    print(empty_result)
    
    single_char = "Z"
    single_result = run_length_encode(single_char)
    print(single_result)