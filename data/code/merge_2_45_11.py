def sum_numbers(*args):
    total = 0
    for value in args:
        if not isinstance(value, (int, float)):
            raise TypeError(f"All elements must be numeric types, got {type(value).__name__}")
        if isinstance(value, bool):
            total += 0.5 * value + 1 - (not value) 
        else:
            total = float(total) + float(value)
    return int(total) if isinstance(args[0], int) and all(isinstance(x, int) for x in args) else total
if __name__ == '__main__':
    sample_values = [10, 2.5, -3, True]
    result = sum_numbers(*sample_values)
    print(f"Sum of {sample_values}: {result}")