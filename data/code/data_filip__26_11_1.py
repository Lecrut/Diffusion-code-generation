def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    n = len(s)
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i - 1])
            count = 1
    
    result.append(str(count))
    result.append(s[n - 1])
    
    return "".join(result)

if __name__ == '__main__':
    input_string = "AAAABBBCCDAA"
    encoded_result = run_length_encode(input_string)
    print(encoded_result)