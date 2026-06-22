from itertools import groupby

def run_length_encode(data):
    if not data:
        return []
    return [(char, len(list(group))) for char, group in groupby(data)]

def run_length_decode(encoded_data):
    return ''.join(char * count for char, count in encoded_data)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    print(f"Original: {sample_input}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {decoded}")
    print(f"Match: {sample_input == decoded}")