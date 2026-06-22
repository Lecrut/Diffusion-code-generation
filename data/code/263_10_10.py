def is_within_range(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound
if __name__ == '__main__':
    print(is_within_range(5, 1, 10))
    print(is_within_range(0, -5, 5))
    print(is_within_range(15, 10, 20))