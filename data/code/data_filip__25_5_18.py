import itertools
import json

def run_length_encode(data: str) -> str:
    if not data:
        return ""
    parts = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        parts.append(f"{count}{key}")
    return "".join(parts)

def run_length_decode(data: str) -> str:
    if not data:
        return ""
    parts = []
    num_str = []
    for char in data:
        if char.isdigit():
            num_str.append(char)
        else:
            count = int("".join(num_str))
            num_str = []
            parts.append(char * count)
    return "".join(parts)

if __name__ == "__main__":
    original = "aabbbccdddd"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(json.dumps({
        "original": original,
        "encoded": encoded,
        "decoded": decoded
    }))