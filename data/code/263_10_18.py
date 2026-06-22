def is_within_range(number, lower_bound, upper_bound):
    if not all(isinstance(i, (int, float)) for i in [number, lower_bound, upper_bound]):
        raise ValueError("All inputs must be numeric values.")
    return lower_bound <= number <= upper_bound

if __name__ == '__main__':
    num = 7
    lower = 5
    upper = 10
    print(is_within_range(num, lower, upper))