from itertools import groupby

def run_length_encode(data: str) -> tuple:
    return tuple(
        (key, len(list(group)))
        for key, group in groupby(data)
    )

if __name__ == '__main__':
    sample_data = "aaabbc"
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)