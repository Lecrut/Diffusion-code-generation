def is_even(n: int) -> bool:
    return n % 2 == 0
if __name__ == '__main__':
    sample_values = [0, 1, 2, -1, -2, -3, 10, -10, 1000000]
    for val in sample_values:
        result = is_even(val)
        print(f'is_even({val}) = {result}')