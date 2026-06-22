from itertools import groupby

def run_length_encode(text):
    if not text:
        return ""
    result = []
    for char, group in groupby(text):
        count = sum(1 for _ in group)
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    text = "aaabbc"
    encoded = run_length_encode(text)
    print(encoded)