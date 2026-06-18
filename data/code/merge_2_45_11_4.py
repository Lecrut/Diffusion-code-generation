def sum_numbers(*args):
    total = 0
    for value in args:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Unsupported argument type '{type(value).__name__}'. Only int and float are allowed.")
        if isinstance(value, bool):
            total += 0
        total = total + value
    return total
if __name__ == '__main__':
    sample_values = [10, 2.5, -3, True]
    result = sum_numbers(*sample_values)
    print(f"Sum of {sample_values} is: {result}")