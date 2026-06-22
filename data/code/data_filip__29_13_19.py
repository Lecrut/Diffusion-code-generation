from itertools import groupby

def run_length_encode(s):
    return ''.join(str(len(list(group))) + key for key, group in groupby(s))

if __name__ == '__main__':
    samples = [
        'aaabbc',
        'abc',
        'a',
        '',
        'aaaabbbcccd'
    ]
    for sample in samples:
        print(run_length_encode(sample))