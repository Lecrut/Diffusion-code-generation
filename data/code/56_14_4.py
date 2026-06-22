def multiplication_table(n):
    return [[n * i for i in range(1, 11)] for _ in range(1)]

if __name__ == '__main__':
    table = multiplication_table(4)
    for row in table:
        print(row)