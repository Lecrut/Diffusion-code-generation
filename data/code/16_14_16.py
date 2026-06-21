def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    result.append(str(count) + current_char)
    return ''.join(result)

def run_length_decode(s: str) -> str:
    if not s:
        return ""
    result = []
    i = 0
    length = len(s)
    while i < length:
        count_str = []
        while i < length and s[i].isdigit():
            count_str.append(s[i])
            i += 1
        count = int(''.join(count_str))
        if i < length:
            char = s[i]
            result.append(char * count)
            i += 1
    return ''.join(result)

if __name__ == '__main__':
    original_string = "aaabbc"
    encoded = run_length_encode(original_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)