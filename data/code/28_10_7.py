from itertools import groupby

def run_length_encode(input_data: str) -> tuple:
    encoded_pairs = []
    for character, group_iterator in groupby(input_data):
        count = sum(1 for _ in group_iterator)
        encoded_pairs.append((character, count))
    return tuple(encoded_pairs)

if __name__ == '__main__':
    sample_string = "aabcccccaaa"
    result = run_length_encode(sample_string)
    print(result)