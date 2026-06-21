def is_strictly_greater(quantity1: int, quantity2: int) -> bool:
    if not isinstance(quantity1, int) or not isinstance(quantity2, int):
        raise ValueError('Both arguments must be integers.')
    return quantity1 > quantity2
if __name__ == '__main__':
    sample_value1 = 15
    sample_value2 = 10
    try:
        result = is_strictly_greater(sample_value1, sample_value2)
        print(result)
    except ValueError as e:
        print(e)