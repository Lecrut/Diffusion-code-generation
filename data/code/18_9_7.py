def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    length = len(s)
    i = 1
    while i < length:
        char = s[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
        i += 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    return "".join(result)

def run_length_decode(s):
    result = []
    length = len(s)
    i = 0
    while i < length:
        char = s[i]
        if char.isdigit():
            j = i
            while j < length and s[j].isdigit():
                j += 1
            count = int(s[i:j])
            i = j
            next_char = s[i]
            result.append(next_char * count)
            i += 1
        else:
            result.append(char)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    input_string = "AAABBBCCCD"
    encoded = run_length_encode(input_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)