def run_length_encoding(s: str) -> str:
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

if __name__ == "__main__":
    input_string = "aaabbccccd"
    compressed_result = run_length_encoding(input_string)
    print(compressed_result)