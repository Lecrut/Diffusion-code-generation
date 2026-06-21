import itertools
import re

def run_length_encode(text: str) -> str:
    if not text:
        return ""

    compressed = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        if count > 1:
            compressed.append(f"{count}{char}")
        else:
            compressed.append(char)

    return "".join(compressed)

if __name__ == "__main__":
    sample_text = "AAABBBCCDAA"
    result = run_length_encode(sample_text)
    print(result)