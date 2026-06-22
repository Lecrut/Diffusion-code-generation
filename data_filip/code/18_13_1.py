def rle_encode(s):
    if not s:
        return []
    current_char = s[0]
    count = 1
    result = []
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1
    result.append((count, current_char))
    return result

def rle_decode(encoded):
    return ''.join(char * count for count, char in encoded)

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCDAA",
        "abcdef",
        "AABBCCCDDDDA",
        "XYZXYZ",
        "OOOOOFFFFFFFFFFF"
    ]
    for sample in sample_strings:
        encoded = rle_encode(sample)
        decoded = rle_decode(encoded)
        print(f"Original: {sample}")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded}")
        print("---")