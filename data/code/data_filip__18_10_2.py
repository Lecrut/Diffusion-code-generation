import itertools

def run_length_encode(input_string):
    return [(char, len(list(group))) for char, group in itertools.groupby(input_string)]

if __name__ == '__main__':
    sample_data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    result = run_length_encode(sample_data)
    print(result)