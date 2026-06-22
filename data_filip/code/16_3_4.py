from itertools import groupby

def run_length_encode(char_list):
    encoded = []
    for key, group in groupby(char_list):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return encoded

if __name__ == '__main__':
    sample_chars = ['a', 'a', 'b', 'b', 'b', 'c']
    result = run_length_encode(sample_chars)
    print(result)