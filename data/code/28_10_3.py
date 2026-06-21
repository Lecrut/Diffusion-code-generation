import itertools

def run_length_encode(data: str) -> tuple:
    if not isinstance(data, str):
        raise TypeError('Input data must be a string.')
    return tuple(((char, len(list(group))) for char, group in itertools.groupby(data)))
if __name__ == '__main__':
    sample_text = 'aabcccccaaa'
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)