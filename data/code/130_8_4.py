def check_sum_zero(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            raise TypeError("Only numeric types (int, float) are supported.")
    return total == 0
if __name__ == '__main__':
    print(check_sum_zero(1, 2, -3))
    print(check_sum_zero(10.5, -5.5, -5))
    print(check_sum_zero(0, 0, 0))
    print(check_sum_zero(1, 1, -2))
    print(check_sum_zero(5))
    try:
        check_sum_zero(1, "a", 0)
    except TypeError as e:
        print(f"Error caught: {e}")