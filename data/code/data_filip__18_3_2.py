import itertools

def run_length_encode(s):
    if not s:
        return ""
    encoded_parts = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        encoded_parts.append(f"{count}{char}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_string = "aaabbcceeee"
    result = run_length_encode(sample_string)
    print(result)