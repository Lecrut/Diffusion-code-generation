def rle_encode(s):
    return ''.join(
        str(len(list(group))) + char for char, group in _rle_generator(s)
    )

def _rle_generator(s):
    if not s:
        return
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            yield current_char, range(count)
            current_char = char
            count = 1
    yield current_char, range(count)

if __name__ == '__main__':
    sample_strings = [
        "AABCCCAA",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        "ABC",
        "AAAAAAAAAA",
        "",
        "XYZXYZ"
    ]
    for sample in sample_strings:
        print(rle_encode(sample))