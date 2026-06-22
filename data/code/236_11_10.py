def multiply_tuple(base_tuple, factor):
    return base_tuple * factor

if __name__ == '__main__':
    sample_base = (1, 2, 3)
    sample_factor = 5
    result = multiply_tuple(sample_base, sample_factor)
    print(result)