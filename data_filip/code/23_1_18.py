import itertools

def run_length_encode(data):
    if not data:
        return []
    return [(char, sum(1 for _ in group)) for char, group in itertools.groupby(data)]

def run_length_decode(encoded_data):
    return ''.join(char * count for char, count in encoded_data)

if __name__ == '__main__':
    sample_string = "aaabbccccddddeee"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    decoded_result = run_length_decode(encoded_result)
    print(decoded_result)