def run_length_encode(data):
    if not data:
        return {}
    
    result = {}
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_string1 = "AAABBBCCDAA"
    sample_string2 = "ABBCDDDEEEEEEFG"
    sample_string3 = ""
    sample_string4 = "ZZZZZZZZ"
    
    print(run_length_encode(sample_string1))
    print(run_length_encode(sample_string2))
    print(run_length_encode(sample_string3))
    print(run_length_encode(sample_string4))