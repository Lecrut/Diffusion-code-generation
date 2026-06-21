import itertools

def run_length_encode(data):
    return tuple((char, len(list(group))) for char, group in itertools.groupby(data))

if __name__ == '__main__':
    sample_data = "aaabbccccdddd"
    result = run_length_encode(sample_data)
    print(result)