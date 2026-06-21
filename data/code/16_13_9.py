import itertools

def run_length_encode(data):
    if not data:
        return []
    result = []
    for key, group in itertools.groupby(data):
        count = len(list(group))
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)