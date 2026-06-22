def multiplication_table(n):
    return [[n * i for i in range(1, 11)]] * 10

if __name__ == '__main__':
    n = 5
    result = multiplication_table(n)
    print(result)