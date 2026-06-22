from itertools import groupby

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    for char, group in groupby(text):
        count = len(list(group))
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded_value = run_length_encode(sample_input)
    print(encoded_value)