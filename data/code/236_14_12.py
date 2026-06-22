from itertools import chain

def validate_input(original_list, n):
    if not isinstance(original_list, list) or not all(isinstance(item, (int, float)) for item in original_list):
        raise ValueError("Original list must contain only numbers.")
    if not isinstance(n, int) or n < 1:
        raise ValueError("N must be a positive integer.")

def concatenate_list(original_list, n):
    validate_input(original_list, n)
    return list(chain.from_iterable([original_list] * n))

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    times = 3
    result = concatenate_list(sample_list, times)
    print(result)