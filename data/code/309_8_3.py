def sum_up_to_n(n):
    if n <= 0:
        return 0
    else:
        return n + sum_up_to_n(n - 1)
if __name__ == '__main__':
    N = 10
    result = sum_up_to_n(N)
    print(result)