from itertools import groupby

def run_length_encode(char_list):
    encoded = []
    for key, group in groupby(char_list):
        count = sum(1 for _ in group)
        encoded.append((count, key))
    return encoded

if __name__ == '__main__':
    sample_list = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
    result = run_length_encode(sample_list)
    print(result)