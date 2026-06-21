from itertools import groupby

def run_length_encode(s):
    return ''.join(str(len(list(group))) + key for key, group in groupby(s))

if __name__ == '__main__':
    sample_string = "aabcccaaa"
    encoded = run_length_encode(sample_string)
    print(encoded)