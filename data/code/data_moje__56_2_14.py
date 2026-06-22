def multiplication_table(n):
    row = []
    for i in range(1, 11):
        row.append(n * i)
    yield row

if __name__ == '__main__':
    num = 7
    result = next(multiplication_table(num))
    print(result)