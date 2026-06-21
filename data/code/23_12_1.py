import itertools

def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbbccdddeff"
    encoded = run_length_encode(sample_string)
    print(encoded)