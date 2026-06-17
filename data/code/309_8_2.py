def sum_up_to(n):
    if n <= 0:
        return 0
    else:
        return n + sum_up_to(n - 1)
if __name__ == '__main__':
    n_value = 10
    result = sum_up_to(n_value)
    print(result)