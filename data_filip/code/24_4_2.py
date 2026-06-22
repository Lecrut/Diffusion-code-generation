import itertools

def run_length_encode(data):
    encoded = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        encoded.append(f"{key}{count}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = run_length_encode(sample_string)
    print(result)