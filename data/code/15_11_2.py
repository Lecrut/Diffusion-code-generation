def run_length_encode(s):
    if not s:
        return ''
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = s[i]
            count = 1
    encoded.append(current_char + str(count))
    return ''.join(encoded)
if __name__ == '__main__':
    test_cases = ['AABBC', 'AAAA', 'ABC', '', 'A', 'AABBCCDD']
    for test in test_cases:
        result = run_length_encode(test)
        print(result)