def compress_string(s):
    if not s:
        return ''
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = char
            count = 1
    compressed.append(current_char + str(count))
    return ''.join(compressed)

if __name__ == '__main__':
    sample1 = 'aaabbbccc'
    sample2 = 'abc'
    sample3 = ''
    sample4 = 'a'
    sample5 = 'aabbbcc'
    print(compress_string(sample1))
    print(compress_string(sample2))
    print(compress_string(sample3))
    print(compress_string(sample4))
    print(compress_string(sample5))