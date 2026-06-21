from itertools import groupby

def run_length_encode(text):
    if not text:
        return ""
    parts = []
    for char, group in groupby(text):
        count = sum(1 for _ in group)
        parts.append(str(count))
        parts.append(char)
    return "".join(parts)

def run_length_decode(encoded):
    if not encoded:
        return ""
    decoded_chars = []
    i = 0
    while i < len(encoded):
        end = i
        while end < len(encoded) and encoded[end].isdigit():
            end += 1
        count_str = encoded[i:end]
        if count_str:
            count = int(count_str)
        else:
            count = 1
        if end < len(encoded):
            char = encoded[end]
            decoded_chars.append(char * count)
            i = end + 1
        else:
            i = end
    return "".join(decoded_chars)

if __name__ == '__main__':
    sample1 = "AAAABBBCCDAA"
    sample2 = "ABC"
    sample3 = ""
    encoded1 = run_length_encode(sample1)
    encoded2 = run_length_encode(sample2)
    encoded3 = run_length_encode(sample3)
    decoded1 = run_length_decode(encoded1)
    decoded2 = run_length_decode(encoded2)
    decoded3 = run_length_decode(encoded3)
    print(encoded1)
    print(encoded2)
    print(encoded3)
    print(decoded1)
    print(decoded2)
    print(decoded3)