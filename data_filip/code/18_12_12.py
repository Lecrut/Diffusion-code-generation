def encode_run_length(s):
    if not s:
        return ''
    
    encoded = []
    char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == char:
            count += 1
        else:
            encoded.append(f"{count}{char}")
            char = s[i]
            count = 1
    
    encoded.append(f"{count}{char}")
    
    return ''.join(encoded)

if __name__ == '__main__':
    print(encode_run_length("aaabbcc"))
    print(encode_run_length(""))
    print(encode_run_length("abcd"))