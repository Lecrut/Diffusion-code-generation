import itertools

def run_length_encode(data):
    groups = itertools.groupby(data)
    return tuple((key, len(list(group))) for key, group in groups)

if __name__ == '__main__':
    sample_data = "WWWWBBWWWWWWBBBBBBB"
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)