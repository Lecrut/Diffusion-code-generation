def check_sum_zero(*args):
    total = 0
    for arg in args:
        total += arg
    return total == 0
if __name__ == '__main__':
    print(check_sum_zero(1, 2, -3))
    print(check_sum_zero(10, -5, -5))
    print(check_sum_zero(0, 0, 0))
    print(check_sum_zero(5.5, -2.5, -3.0))
    print(check_sum_zero(1, 1, -2))
    print(check_sum_zero())
    print(check_sum_zero(100))