import itertools
import json

def rle_encode(text: str) -> str:
    if not text:
        return ""
    groups = itertools.groupby(text)
    result = []
    for char, group in groups:
        count = sum(1 for _ in group)
        if count > 1:
            result.append(f"{count}{char}")
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    input_text = "aaabbcccc"
    encoded = rle_encode(input_text)
    print(encoded)