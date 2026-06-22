from itertools import groupby

RLE_MARKER = "RLE:"

def rle_encode(source):
    if not source:
        return ""
    parts = []
    for char, group in groupby(source):
        length = len(list(group))
        parts.append(str(length))
        parts.append(char)
    return RLE_MARKER + "".join(parts)

def rle_decode(encoded):
    if not encoded:
        return ""
    if not encoded.startswith(RLE_MARKER):
        raise ValueError("Invalid RLE format: missing marker")
    payload = encoded[len(RLE_MARKER):]
    if not payload:
        return ""
    decoded = []
    i = 0
    n = len(payload)
    while i < n:
        num_end = i
        while num_end < n and not payload[num_end].isalpha():
            num_end += 1
        if num_end == i:
            i += 1
            continue
        count_str = payload[i:num_end]
        if not count_str:
            i = num_end
            continue
        try:
            count = int(count_str)
        except ValueError:
            i = num_end
            continue
        if num_end < n:
            char = payload[num_end]
            decoded.append(char * count)
            i = num_end + 1
        else:
            i = num_end
    return "".join(decoded)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    compressed = rle_encode(sample_text)
    print(compressed)
    decompressed = rle_decode(compressed)
    print(decompressed)
    empty_text = ""
    c_empty = rle_encode(empty_text)
    print(c_empty)
    d_empty = rle_decode(c_empty)
    print(d_empty)
    single_char = "X"
    c_single = rle_encode(single_char)
    print(c_single)
    d_single = rle_decode(c_single)
    print(d_single)
    mixed_text = "abcdef"
    c_mixed = rle_encode(mixed_text)
    print(c_mixed)
    d_mixed = rle_decode(c_mixed)
    print(d_mixed)
    long_run = "A" * 1000
    c_long = rle_encode(long_run)
    print(c_long)
    d_long = rle_decode(c_long)
    print(len(d_long))