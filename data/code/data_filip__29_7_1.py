def run_length_encode(s):
    if not s:
        return ''
    encoded = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = char
            count = 1
    encoded.append(current_char + str(count))
    return ''.join(encoded)

if __name__ == '__main__':
    print(run_length_encode('AAABBBCCD'))
    print(run_length_encode('ABC'))
    print(run_length_encode(''))
    print(run_length_encode('AAAAAAAAAA'))
    print(run_length_encode('A'))
    print(run_length_encode('AABBCC'))