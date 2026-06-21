from itertools import groupby

def run_length_encode(data):
    return [(len(list(group)), key) for key, group in groupby(data)]

if __name__ == '__main__':
    sample_data = "aaabbccccd"
    result = run_length_encode(sample_data)
    print(result)