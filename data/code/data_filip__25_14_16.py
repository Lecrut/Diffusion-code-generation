import itertools

def run_length_encode(s: str) -> str:
    if not s:
        return ""
    encoded = []
    for char, group in itertools.groupby(s):
        length = len(list(group))
        encoded.append(f"{length}{char}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_string = "aaabbccc"
    result = run_length_encode(sample_string)
    print(result)