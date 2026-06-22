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
            encoded.append(f'{count}{current_char}')
            current_char = char
            count = 1
    encoded.append(f'{count}{current_char}')
    return ''.join(encoded)

def run_length_decode(s):
    if not s:
        return ''
    decoded = []
    i = 0
    while i < len(s):
        count_str = ''
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        count = int(count_str)
        char = s[i]
        i += 1
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample1 = 'AAABBBCCD'
    sample2 = 'AABBCC'
    sample3 = ''
    sample4 = 'A'
    sample5 = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))

    encoded1 = run_length_encode(sample1)
    print(run_length_decode(encoded1))

    encoded5 = run_length_encode(sample5)
    print(run_length_decode(encoded5))