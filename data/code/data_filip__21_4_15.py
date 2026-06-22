def run_length_encoding(data):
    if not data:
        return {}
    
    result = {}
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = data[i]
            count = 1
    
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_string = "aaabbcddddd"
    encoded = run_length_encoding(sample_string)
    print(encoded)
    
    sample_string2 = "hello"
    encoded2 = run_length_encoding(sample_string2)
    print(encoded2)
    
    sample_string3 = ""
    encoded3 = run_length_encoding(sample_string3)
    print(encoded3)
    
    sample_string4 = "a"
    encoded4 = run_length_encoding(sample_string4)
    print(encoded4)