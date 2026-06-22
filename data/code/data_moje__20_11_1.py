def is_even(number: int) -> bool:
    if not isinstance(number, int):
        return False
    return number % 2 == 0
if __name__ == '__main__':
    sample_values = [-2, -1, 0, 1, 2]
    results = [(val, is_even(val)) for val in sample_values]
    for value, result in results:
        print(result)