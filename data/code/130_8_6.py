def check_sum_zero(*args):
    total = 0
    for arg in args:
        try:
            total += arg
        except TypeError:
            return False
    return total == 0
if __name__ == '__main__':
    print(check_sum_zero(1, 2, -3))
    print(check_sum_zero(5, -5, 10))
    print(check_sum_zero(1, 1, -2))
    print(check_sum_zero(0, 0, 0))
    print(check_sum_zero(10.5, -5.5, 0))
    print(check_sum_zero(1, 2, 3, 4))
    print(check_sum_zero(1, "a", 2))
    print(check_sum_zero())
    print(check_sum_zero(10))