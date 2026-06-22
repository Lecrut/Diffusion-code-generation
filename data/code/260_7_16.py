def filter_complex_numbers(complex_set):
    if not all(isinstance(c, complex) for c in complex_set):
        raise ValueError("All elements must be complex numbers")
    return {c for c in complex_set if c.real > 0 and c.imag > 0}

if __name__ == '__main__':
    sample_set = {3+4j, -1-2j, 5+6j, 7-8j}
    filtered_set = filter_complex_numbers(sample_set)
    print(filtered_set)