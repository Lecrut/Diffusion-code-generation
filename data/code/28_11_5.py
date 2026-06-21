def run_length_encode(s):
    if not s:
        return ''
    if len(s) == 1:
        return s
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    
    return ''.join(encoded)

if __name__ == '__main__':
    print(run_length_encode(''))
    print(run_length_encode('a'))
    print(run_length_encode('aaabbbcca'))
    print(run_length_encode('abcdef'))
    print(run_length_encode('aaaa'))