def is_within_range(value, lower_bound, upper_bound):
    return lower_bound <= value <= upper_bound
if __name__ == '__main__':
    print(is_within_range(5, 1, 10))
    print(is_within_range(-1, 0, 5))
    print(is_within_range(7, 7, 7))