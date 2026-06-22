def encode_string(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        if not (char.isalnum()):
            i += 1
            continue
        count = 0
        while i < len(s) and s[i] == char and s[i].isalnum():
            count += 1
            i += 1
        result.append((char, count))
    encoded_dict = {}
    for char, count in result:
        encoded_dict[char] = count
    return encoded_dict

if __name__ == '__main__':
    sample_input = "aaabbb2233c"
    output = encode_string(sample_input)
    print(output)