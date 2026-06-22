import itertools

def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{count}{key}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccc"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)