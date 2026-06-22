from itertools import groupby

def run_length_encode(char_list):
    encoded = []
    for key, group in groupby(char_list):
        count = len(list(group))
        encoded.append((key, count))
    return encoded

if __name__ == '__main__':
    sample_chars = ['a', 'a', 'b', 'b', 'b', 'c']
    result = run_length_encode(sample_chars)
    print(result)