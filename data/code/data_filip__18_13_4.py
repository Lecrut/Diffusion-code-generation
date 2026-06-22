def rle_encode(text):
    if not text:
        return []
    pairs = []
    ref_char = text[0]
    run_len = 1
    for idx in range(1, len(text)):
        if text[idx] == ref_char:
            run_len += 1
        else:
            pairs.append((run_len, ref_char))
            ref_char = text[idx]
            run_len = 1
    pairs.append((run_len, ref_char))
    return pairs

def rle_decode(pairs):
    return ''.join(char * count for count, char in pairs)

if __name__ == '__main__':
    sample_a = "AAABBBCCD"
    encoded_a = rle_encode(sample_a)
    decoded_a = rle_decode(encoded_a)
    print(encoded_a)
    print(decoded_a)
    sample_b = "XYZ"
    encoded_b = rle_encode(sample_b)
    decoded_b = rle_decode(encoded_b)
    print(encoded_b)
    print(decoded_b)