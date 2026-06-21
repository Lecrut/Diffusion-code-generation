import itertools

def run_length_encode(iterable):
    return [(char, len(list(group))) for char, group in itertools.groupby(iterable)]

if __name__ == '__main__':
    data = 'AAABBBCCCC'
    result = run_length_encode(data)
    print(result)