from itertools import groupby

def run_length_encode(s: str) -> str:
    result = []
    for key, group in groupby(s):
        length = len(list(group))
        result.append(f"{length}{key}")
    return "".join(result)

if __name__ == '__main__':
    input_string = "aaabbc"
    encoded = run_length_encode(input_string)
    print(encoded)