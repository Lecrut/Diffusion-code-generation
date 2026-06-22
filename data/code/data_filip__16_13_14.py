import itertools

def run_length_encode(int_list):
    if not int_list:
        return []
    result = []
    for key, group in itertools.groupby(int_list):
        count = len(list(group))
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5]
    print(run_length_encode(sample_data))