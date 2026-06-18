from functools import reduce
def remove_if(condition_func, collection):
    return [item for item in collection if not condition_func(item)]
def is_even(x):
    return x % 2 == 0
if __name__ == '__main__':
    sample_collection = list(range(1, 26))
    filtered_result = remove_if(is_even, sample_collection)
    print(filtered_result[:5])