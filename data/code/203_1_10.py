def is_greater(quantity1: int, quantity2: int) -> bool:
    if not isinstance(quantity1, int) or not isinstance(quantity2, int):
        raise ValueError('Both arguments must be integers.')
    return quantity1 > quantity2
if __name__ == '__main__':
    sample_value1 = 5
    sample_value2 = 3
    result = is_greater(sample_value1, sample_value2)
    print(result)