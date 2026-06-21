from itertools import groupby

def run_length_encode(text):
    if not text:
        return []
    return [(char, len(list(group))) for char, group in groupby(text)]

if __name__ == '__main__':
    sample_string = "aaabbccccdddddeee"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)