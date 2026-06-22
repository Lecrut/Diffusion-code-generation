from itertools import chain

def double_and_concatenate(original):
    return list(chain.from_iterable([original] * 2))

if __name__ == '__main__':
    sample_list = [4, 5, 6]
    result = double_and_concatenate(sample_list)
    print(result)