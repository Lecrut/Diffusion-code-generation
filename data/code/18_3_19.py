import itertools

def run_length_encode(s):
    encoded = []
    for key, group in itertools.groupby(s):
        count = len(list(group))
        encoded.append(f"{key}{count}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_string = "aaabbcccc"
    result = run_length_encode(sample_string)
    print(result)