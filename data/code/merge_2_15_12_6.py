import sys
def sort_numerical_data(data):
    if not data:
        return []
    try:
        sorted_data = sorted(data)
        return sorted_data
    except TypeError as e:
        raise ValueError("All elements in the input list must be comparable.") from e
if __name__ == '__main__':
    sample_integers = [64, 34, 25, 12, 22, 11, 90]
    sample_floats = [3.14, -2.718, 0.0, 42.0, -1e-5]
    result_int = sort_numerical_data(sample_integers)
    result_float = sort_numerical_data(sample_floats)
    print("Sorted Integers:", result_int)
    print("Sorted Floats:", result_float)