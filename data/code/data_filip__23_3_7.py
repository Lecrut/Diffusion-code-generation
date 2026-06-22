import itertools

def encode_rle(text):
    if not text:
        return ""
    encoded_parts = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        encoded_parts.append(f"{count}{char}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = encode_rle(sample_text)
    print(result)