import re

def decode_rle(encoded: str) -> str:
    if not encoded:
        return ""
    pattern = re.compile(r'(\d*)(.)')
    results = []
    for match in pattern.finditer(encoded):
        count_str = match.group(1)
        char = match.group(2)
        if count_str == '':
            count = 1
        else:
            count = int(count_str)
        results.append(char * count)
    return ''.join(results)

if __name__ == '__main__':
    samples = [
        "3a2b1c",
        "10z",
        "a",
        "2x3y4z",
        "",
        "100A2B",
        "3",
        "a2b"
    ]
    for sample in samples:
        print(f"decode_rle('{sample}') = '{decode_rle(sample)}'")