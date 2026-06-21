def run_length_encode(s):
    if not s:
        return []
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append((s[i - 1], count))
            count = 1
    result.append((s[-1], count))
    return result

def run_length_encode_gen(s):
    if not s:
        return
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            yield (s[i - 1], count)
            count = 1
    yield (s[-1], count)

def run_length_decode(encoded):
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    encoded_list = run_length_encode(sample)
    print(encoded_list)
    encoded_gen = list(run_length_encode_gen(sample))
    print(encoded_gen)
    decoded = run_length_decode(encoded_list)
    print(decoded)