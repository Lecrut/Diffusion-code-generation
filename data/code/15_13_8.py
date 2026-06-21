def compress_string(s: str) -> str:
    if not s:
        return ""
    
    result = []
    count = 1
    n = len(s)
    
    for i in range(n):
        if i + 1 < n and s[i] == s[i + 1]:
            count += 1
        else:
            result.append(s[i])
            if count > 1:
                result.append(str(count))
            count = 1
    
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbcdddddd"
    output = compress_string(sample_input)
    print(output)
    
    sample_input_two = "abcdef"
    output_two = compress_string(sample_input_two)
    print(output_two)
    
    sample_input_three = ""
    output_three = compress_string(sample_input_three)
    print(output_three)
    
    sample_input_four = "aaaa"
    output_four = compress_string(sample_input_four)
    print(output_four)