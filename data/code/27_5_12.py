import sys
sys.setrecursionlimit(2000)

def rle_encode_zip(s):
    if not s:
        return ""
    shifted = s[1:] + "\x00"
    result = []
    current_char = s[0]
    count = 1
    pairs = list(zip(s, shifted))
    for current, next_char in pairs:
        if current == next_char:
            count += 1
        else:
            result.append(f"{count}{current}")
            count = 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAAAABBBS"
    encoded = rle_encode_zip(sample_input)
    print(encoded)