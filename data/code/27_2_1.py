import itertools

def run_length_encode(iterable):
    for key, group in itertools.groupby(iterable):
        count = sum(1 for _ in group)
        yield (key, count)

if __name__ == '__main__':
    result = list(run_length_encode('AAABBBCCCC'))
    print(result)