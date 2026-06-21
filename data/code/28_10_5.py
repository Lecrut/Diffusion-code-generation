import itertools

def run_length_encode(data: str) -> tuple:
    groups = itertools.groupby(data)
    result = tuple((char, len(list(group))) for char, group in groups)
    return result

if __name__ == '__main__':
    sample_data = "aaabbbcccaabb"
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)