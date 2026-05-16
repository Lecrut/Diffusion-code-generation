def check_sum_zero(*args):
    total = 0
    for arg in args:
        try:
            total += arg
        except TypeError:
            pass
    return total == 0
if __name__ == '__main__':
    print(check_sum_zero(1, 2, -3))
    print(check_sum_zero(5, -5, 10))
    print(check_sum_zero(0, 0, 0))
    print(check_sum_zero(1.5, -1.5, 0))
    print(check_sum_zero(10, 20, -30, 0.1))
    print(check_sum_zero())
    print(check_sum_zero(1, 2, 3))
    print(check_sum_zero(1, 2, -1, 0.5))