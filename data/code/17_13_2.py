def run_length_encode(s):
    if not s:
        return ''
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    return ''.join(result)

def run_length_decode(s):
    if not s:
        return ''
    result = []
    i = 0
    while i < len(s):
        count_str = ''
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        count = int(count_str) if count_str else 1
        char = s[i]
        result.append(char * count)
        i += 1
    return ''.join(result)

if __name__ == '__main__':
    samples = ['AABBBCCCC', 'Hello World!!!', 'AAAAAAAA', 'XYZ', 'A']
    for sample in samples:
        encoded = run_length_encode(sample)
        decoded = run_length_decode(encoded)
        print(encoded)
        print(decoded)