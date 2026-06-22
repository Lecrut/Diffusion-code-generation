def run_length_encode(s):
    if not s:
        return ''
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
    result.append(str(count) + s[-1])
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
        i += 1
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = 'aaaabbbcccd'
    encoded = run_length_encode(sample_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)