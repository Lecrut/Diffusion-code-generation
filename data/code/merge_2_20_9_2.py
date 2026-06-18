import timeit
def filter_positive_advanced(values: list) -> list:
    return [x for x in values if not (lambda v: v < 0)(x)]
if __name__ == '__main__':
    sample_data = [-5, -3.2, 10, -7, 4.8]
    result = filter_positive_advanced(sample_data)
    print(result)