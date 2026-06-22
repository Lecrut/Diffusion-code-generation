def run_length_encode(data):
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = data[i]
            count = 1
    
    encoded.append(current_char + str(count))
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_input_1 = "AAABBC"
    sample_input_2 = "A"
    sample_input_3 = ""
    sample_input_4 = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    
    result_1 = run_length_encode(sample_input_1)
    result_2 = run_length_encode(sample_input_2)
    result_3 = run_length_encode(sample_input_3)
    result_4 = run_length_encode(sample_input_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)