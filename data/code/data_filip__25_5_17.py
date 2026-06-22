import itertools

def run_length_encode(data):
    return [(key, len(list(group))) for key, group in itertools.groupby(data)]

if __name__ == '__main__':
    sample_input = "aaabbccccdddd"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    sample_list = [1, 1, 2, 2, 2, 3]
    list_result = run_length_encode(sample_list)
    print(list_result)