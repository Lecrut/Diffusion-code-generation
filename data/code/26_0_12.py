import itertools

def run_length_encode(input_string: str) -> list:
    if not input_string:
        return []
    encoded = []
    for char, group in itertools.groupby(input_string):
        count = sum((1 for _ in group))
        encoded.append((char, count))
    return encoded
if __name__ == '__main__':
    sample_string = 'aaabbc'
    result = run_length_encode(sample_string)
    print(result)