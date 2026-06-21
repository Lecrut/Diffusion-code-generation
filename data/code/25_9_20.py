import itertools

def run_length_encode(data):
    if not data:
        return ""
    chunks = []
    for char, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        chunks.append(f"{count}{char}")
    return "".join(chunks)

if __name__ == '__main__':
    sample = "AAABBBCCDAA"
    result = run_length_encode(sample)
    print(result)