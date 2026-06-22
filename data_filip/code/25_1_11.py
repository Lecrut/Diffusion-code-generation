def run_length_encode(s):
    if not s:
        return ''
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return ''.join(encoded)

if __name__ == '__main__':
    sample1 = 'aaabbbcc'
    print(run_length_encode(sample1))
    
    sample2 = 'abc'
    print(run_length_encode(sample2))
    
    sample3 = 'aaaabbbbccccc'
    print(run_length_encode(sample3))
    
    sample4 = ''
    print(run_length_encode(sample4))
    
    sample5 = 'a'
    print(run_length_encode(sample5))