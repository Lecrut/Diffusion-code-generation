import itertools

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    for key, group in itertools.groupby(data):
        count = sum((1 for _ in group))
        encoded.append((key, count))
    return encoded
if __name__ == '__main__':
    sample_data = 'AAABBBCCDAA'
    result = run_length_encode(sample_data)
    print(result)
    sample_data2 = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    result2 = run_length_encode(sample_data2)
    print(result2)
    sample_data3 = 'abc'
    result3 = run_length_encode(sample_data3)
    print(result3)
    sample_data4 = ''
    result4 = run_length_encode(sample_data4)
    print(result4)