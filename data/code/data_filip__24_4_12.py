import itertools

def run_length_encode(data: str) -> str:
    groups = itertools.groupby(data)
    encoded = []
    for char, group in groups:
        count = sum(1 for _ in group)
        encoded.append(f"{count}{char}")
    return "".join(encoded)

if __name__ == '__main__':
    text = "AAABBBCCCD"
    result = run_length_encode(text)
    print(result)