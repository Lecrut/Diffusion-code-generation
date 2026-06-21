import itertools

def run_length_encode(iterable):
    return ((key, len(list(group))) for key, group in itertools.groupby(iterable))

if __name__ == '__main__':
    data = 'AAABBBCCCC'
    result = list(run_length_encode(data))
    print(result)