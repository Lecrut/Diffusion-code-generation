def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = input_string[i]
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample1 = "AAABBBCCD"
    print(run_length_encode(sample1))
    
    sample2 = "ABCDE"
    print(run_length_encode(sample2))
    
    sample3 = "AABBCC"
    print(run_length_encode(sample3))
    
    sample4 = ""
    print(run_length_encode(sample4))
    
    sample5 = "AAAAAABBBBBBCCCCCC"
    print(run_length_encode(sample5))