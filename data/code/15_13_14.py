import sys

def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    length = len(s)
    
    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1
    
    result.append(s[length - 1])
    if count > 1:
        result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcddddde"
    compressed_output = compress_string(sample_input)
    print(compressed_output)