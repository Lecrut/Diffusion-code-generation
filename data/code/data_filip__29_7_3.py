def run_length_encode(s):
    if not s:
        return ""
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

if __name__ == '__main__':
    print(run_length_encode("AAABBBCCD"))
    print(run_length_encode("ABC"))
    print(run_length_encode(""))
    print(run_length_encode("A"))
    print(run_length_encode("EEEEEEEFG"))
    print(run_length_encode("aAaAaA"))
    print(run_length_encode("111223333"))
    print(run_length_encode("!@@##$$"))