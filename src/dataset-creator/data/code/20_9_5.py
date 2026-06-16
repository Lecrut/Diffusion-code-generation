import timeit
def filter_positive_advanced(values: list) -> list:
    return [x for x in values if not (lambda v: v < 0)(x)]
if __name__ == '__main__':
    sample_data = [-5, -2.3, 10, 4, -7, 8]
    result = filter_positive_advanced(sample_data)
    print(result)