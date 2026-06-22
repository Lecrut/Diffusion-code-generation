import itertools

def run_length_encode(s):
    result = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)