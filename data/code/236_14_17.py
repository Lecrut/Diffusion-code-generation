from itertools import chain

def repeat_list(original, n):
    return list(chain.from_iterable([original] * n))

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3]
    TIMES = 3
    result = repeat_list(SAMPLE_LIST, TIMES)
    print(result)