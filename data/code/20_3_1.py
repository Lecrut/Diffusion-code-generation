def run_length_encode(input_string):
    if not input_string:
        return ""
    
    compressed = []
    count = 1
    char = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] == char:
            count += 1
        else:
            compressed.append(f"{count}{char}")
            char = input_string[i]
            count = 1
    
    compressed.append(f"{count}{char}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_input = "aaabbbcccd"
    result = run_length_encode(sample_input)
    print(result)