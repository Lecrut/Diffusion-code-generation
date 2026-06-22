from itertools import groupby

def run_length_encoded(iterable):
    return [(char, sum(1 for _ in group)) for char, group in groupby(iterable)]

if __name__ == '__main__':
    result = run_length_encoded('AAABBBCCCC')
    print(result)