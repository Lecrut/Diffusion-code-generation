def sum_of_integers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_integers(n - 1)
if __name__ == '__main__':
    number = 10
    result = sum_of_integers(number)
    print(result)