from itertools import groupby

def run_length_encode(s: str) -> str:
    result = []
    for char, group in groupby(s):
        count = len(list(group))
        if count == 1:
            result.append(char)
        else:
            result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    text = "AAABBBCCCDAA"
    encoded = run_length_encode(text)
    print(encoded)