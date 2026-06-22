def run_length_encode(s):
    if not s:
        return ''
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1])
            if count > 1:
                result.append(str(count))
            count = 1
    result.append(s[-1])
    if count > 1:
        result.append(str(count))
    return ''.join(result)

if __name__ == '__main__':
    print(run_length_encode('aaabbc'))
    print(run_length_encode('aabcccccaaa'))
    print(run_length_encode(''))
    print(run_length_encode('a'))
    print(run_length_encode('abcdef'))
    print(run_length_encode('aabbcc'))