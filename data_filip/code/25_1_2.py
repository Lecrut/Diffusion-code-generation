def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(str(count))
            compressed.append(s[i - 1])
            count = 1
    
    compressed.append(str(count))
    compressed.append(s[-1])
    
    return "".join(compressed)

if __name__ == "__main__":
    sample_input = "aaabbcdeeee"
    result = compress_string(sample_input)
    print(result)
    
    sample_input_2 = "a"
    result_2 = compress_string(sample_input_2)
    print(result_2)
    
    sample_input_3 = ""
    result_3 = compress_string(sample_input_3)
    print(result_3)