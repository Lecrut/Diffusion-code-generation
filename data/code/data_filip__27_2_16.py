import itertools

def run_length_encode(iterable):
    for key, group in itertools.groupby(iterable):
        yield (len(list(group)), key)

if __name__ == '__main__':
    data = 'AAABBBCCCC'
    result = list(run_length_encode(data))
    print(result)