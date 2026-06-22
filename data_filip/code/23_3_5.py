from itertools import groupby

def encode_text(text):
    if not text:
        return ""
    encoded = []
    for char, group in groupby(text):
        count = len(list(group))
        encoded.append(f"{char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = encode_text(sample_text)
    print(result)