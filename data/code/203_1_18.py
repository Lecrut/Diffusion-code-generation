def is_first_greater(quantity1: int, quantity2: int) -> bool:
    if not isinstance(quantity1, int) or not isinstance(quantity2, int):
        raise ValueError('Both arguments must be integers.')
    return quantity1 > quantity2
if __name__ == '__main__':
    sample_quantity1 = 42
    sample_quantity2 = 30
    result = is_first_greater(sample_quantity1, sample_quantity2)
    print(result)