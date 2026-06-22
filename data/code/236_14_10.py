import itertools

def concatenate_list(original, n):
    return list(itertools.chain.from_iterable([original] * n))
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    n = 3
    result = concatenate_list(sample_list, n)
    print(result)