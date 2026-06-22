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
            encoded.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    encoded.append(str(count) + current_char)
    return ''.join(encoded)

def run_length_decode(encoded):
    if not encoded:
        return ''
    decoded = []
    i = 0
    while i < len(encoded):
        count_str = ''
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        char = encoded[i]
        i += 1
        count = int(count_str) if count_str else 1
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample_input = 'aaaabbcdeeeffffg'
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(decoded == sample_input)