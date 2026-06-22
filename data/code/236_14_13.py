from itertools import chain

def concatenate_list(original_list, N):
    return list(chain.from_iterable([original_list] * N))

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    N = 3
    result = concatenate_list(sample_list, N)
    print(result)