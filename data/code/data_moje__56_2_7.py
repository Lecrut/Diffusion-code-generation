def multiplication_table(n):
    for i in range(1, 11):
        yield f"{n} * {i} = {n * i}"

if __name__ == '__main__':
    n = 7
    for row in multiplication_table(n):
        print(row)