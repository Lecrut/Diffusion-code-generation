import timeit
def sort_numerical_data(data):
    if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
        return sorted(data)
    elif isinstance(data, tuple) and all(isinstance(x, (int, float)) for x in data):
        return type(data)(sorted(data))
    else:
        raise TypeError("Input must be a list or tuple of numerical values.")
if __name__ == '__main__':
    sample_list = [54321, 98765, -100, 3.14, None] if False else [54321, 98765, -100, 3.14, 12345]
    sample_tuple = (54321, 98765, -100, 3.14)
    result_list = sort_numerical_data(sample_list)
    result_tuple = sort_numerical_data(sample_tuple)
    print(result_list)
    print(result_tuple)