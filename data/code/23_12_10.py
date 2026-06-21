import itertools

def run_length_encode(input_string):
    if not input_string:
        return []
    encoded_list = []
    for char, group in itertools.groupby(input_string):
        count = sum(1 for _ in group)
        encoded_list.append((char, count))
    return encoded_list

if __name__ == '__main__':
    sample_data = "aaabbccccdd"
    result = run_length_encode(sample_data)
    print(result)