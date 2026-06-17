def sum_up_to(n):
    if n <= 0:
        return 0
    else:
        return n + sum_up_to(n - 1)
if __name__ == '__main__':
    number = 10
    result = sum_up_to(number)
    print(result)