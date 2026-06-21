import re

def run_length_encode(s):
    if not s:
        return ''
    encoded = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    return ''.join(encoded)

def is_compression_effective(original):
    encoded = run_length_encode(original)
    return len(encoded) < len(original)

if __name__ == '__main__':
    sample1 = 'aaaabbbcc'
    result1 = is_compression_effective(sample1)
    print(result1)
    sample2 = 'abcdefg'
    result2 = is_compression_effective(sample2)
    print(result2)
    sample3 = 'aabb'
    result3 = is_compression_effective(sample3)
    print(result3)