def run_length_encode(s):
    if not s:
        return ''
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1
    result.append(current_char)
    result.append(str(count))
    compressed = ''.join(result)
    if len(compressed) >= len(s):
        return s
    return compressed

if __name__ == '__main__':
    sample1 = 'AAABBBCC'
    sample2 = 'AABB'
    sample3 = ''
    sample4 = 'ABCD'
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))