def sum_tuple_elements(float_tuple):
    if not all(isinstance(x, float) for x in float_tuple):
        raise ValueError("All elements in the tuple must be floats.")
    return sum(float_tuple)

if __name__ == '__main__':
    sample_tuple = (3.5, 2.1, 4.8)
    print(sum_tuple_elements(sample_tuple))