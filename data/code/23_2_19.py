def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

def run_length_decode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        count = int(num_str)
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)