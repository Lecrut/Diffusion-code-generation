def multiplication_table_generator(n):
    i = 1
    while i <= 10:
        yield (n, i, n * i)
        i += 1

if __name__ == '__main__':
    for row in multiplication_table_generator(5):
        print(row)