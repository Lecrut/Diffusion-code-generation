def sum_two_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    sample_values = {1: 3, 2: 5}
    result = sum_two_numbers(sample_values[1], sample_values[2])
    print(result)