def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    count = 1
    length = len(input_string)
    
    for i in range(1, length):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append(f"{count}{input_string[i - 1]}")
            count = 1
    result.append(f"{count}{input_string[-1]}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaaa"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)