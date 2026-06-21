def run_length_encoding(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char + str(count))
    
    return "".join(result)

if __name__ == '__main__':
    test_input = "aaabbccccd"
    compressed = run_length_encoding(test_input)
    print(compressed)
    
    test_input2 = "aA111bbCCc"
    compressed2 = run_length_encoding(test_input2)
    print(compressed2)
    
    test_input3 = ""
    compressed3 = run_length_encoding(test_input3)
    print(compressed3)