import itertools

def run_length_encode(data: str) -> list[tuple[int, str]]:
    encoded = []
    for key, group in itertools.groupby(data):
        run_length = sum((1 for _ in group))
        encoded.append((run_length, key))
    return encoded
if __name__ == '__main__':
    sample_data = 'AAABBBCCDAA'
    result = run_length_encode(sample_data)
    print(result)
    sample_data2 = 'ABC'
    result2 = run_length_encode(sample_data2)
    print(result2)
    sample_data3 = 'AAAAAAAAA'
    result3 = run_length_encode(sample_data3)
    print(result3)