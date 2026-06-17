def check_sum_even(a, b):
    return (a + b) % 2 == 0
if __name__ == '__main__':
    print(check_sum_even(4, 6))
    print(check_sum_even(3, 5))
    print(check_sum_even(10, 2))