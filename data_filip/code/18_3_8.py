import itertools

def run_length_encode(s):
    encoded = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        encoded.append(f"{key}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    result = run_length_encode(sample_string)
    print(result)