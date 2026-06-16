def check_sum_even(a, b):
    return (a + b) % 2 == 0
if __name__ == '__main__':
    print(check_sum_even(2, 4))
    print(check_sum_even(3, 5))
    print(check_sum_even(6, 0))
    print(check_sum_even(7, 1))