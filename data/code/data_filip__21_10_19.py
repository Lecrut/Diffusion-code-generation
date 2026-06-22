import itertools

def run_length_encode(data):
    if not data:
        return []

    encoded = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return encoded

def run_length_decode(encoded_data):
    decoded = []
    for key, count in encoded_data:
        decoded.extend([key] * count)
    return decoded

if __name__ == '__main__':
    sample_string = "AAABBBCCCDAA"
    sample_list = [1, 1, 2, 3, 3, 3, 2, 2, 1]

    encoded_string = run_length_encode(sample_string)
    print(encoded_string)

    decoded_string = run_length_decode(encoded_string)
    print(decoded_string)

    encoded_list = run_length_encode(sample_list)
    print(encoded_list)

    decoded_list = run_length_decode(encoded_list)
    print(decoded_list)