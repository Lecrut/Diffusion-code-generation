def sum_three_floats(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7]
    result = sum_three_floats(*sample_values)
    print(result)