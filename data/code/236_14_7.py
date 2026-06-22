from itertools import chain
MULTIPLIER = 3

def concatenate_list(original, n):
    return list(chain.from_iterable([original] * n))
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    result = concatenate_list(sample_list, MULTIPLIER)
    print(result)