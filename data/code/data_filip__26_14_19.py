def run_length_encoding(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    compressed_output = run_length_encoding(sample_input)
    print(compressed_output)
    
    sample_input_2 = "a1b2c3"
    compressed_output_2 = run_length_encoding(sample_input_2)
    print(compressed_output_2)
    
    sample_input_3 = "AaBbCc"
    compressed_output_3 = run_length_encoding(sample_input_3)
    print(compressed_output_3)
    
    sample_input_4 = ""
    compressed_output_4 = run_length_encoding(sample_input_4)
    print(compressed_output_4)