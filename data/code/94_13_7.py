from itertools import islice

def any_item_satisfies(iterable, predicate):
    return any(predicate(item) for item in iterable)

if __name__ == '__main__':
    sample_sequence = [2, 4, 6, 8, 10]
    sample_predicate = lambda x: x % 3 == 0
    result = any_item_satisfies(sample_sequence, sample_predicate)
    print(result)