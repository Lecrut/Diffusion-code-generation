def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

def run_length_decode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        if i < len(s):
            char = s[i]
            i += 1
            result.append(char * count)
    return "".join(result)

if __name__ == "__main__":
    sample1 = "AAAABBBCCDAA"
    encoded1 = run_length_encode(sample1)
    print(encoded1)

    sample2 = "ABC"
    encoded2 = run_length_encode(sample2)
    print(encoded2)

    sample3 = "AABBCCDD"
    encoded3 = run_length_encode(sample3)
    print(encoded3)

    decoded1 = run_length_decode(encoded1)
    print(decoded1)

    empty_str = ""
    encoded_empty = run_length_encode(empty_str)
    print(encoded_empty)

    single_char = "X"
    encoded_single = run_length_encode(single_char)
    print(encoded_single)

    decoded_single = run_length_decode(encoded_single)
    print(decoded_single)