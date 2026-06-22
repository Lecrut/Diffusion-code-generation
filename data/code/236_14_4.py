from itertools import chain

def repeat_list(original, n):
    if not isinstance(original, list) or not all(isinstance(item, (int, float)) for item in original):
        raise ValueError("Original must be a list of numbers")
    if not isinstance(n, int) or n < 0:
        raise ValueError("N must be a non-negative integer")
    
    return list(chain.from_iterable([original] * n))

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    times = 3
    result = repeat_list(sample_list, times)
    print(result)