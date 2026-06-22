from itertools import chain

def concatenate_list(original, n):
    return list(chain.from_iterable([original] * n))

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    times = 3
    result = concatenate_list(sample_list, times)
    print(result)