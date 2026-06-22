from itertools import groupby

def run_length_encode(iterable):
    return [(char, len(list(group))) for char, group in groupby(iterable)]

if __name__ == '__main__':
    result = run_length_encode('AAABBBCCCC')
    print(result)