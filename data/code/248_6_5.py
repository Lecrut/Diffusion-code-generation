def sum_up_to_n(n):
    if n <= 0:
        return 0
    else:
        return n + sum_up_to_n(n - 1)
if __name__ == '__main__':
    number = 5
    result = sum_up_to_n(number)
    print(result)