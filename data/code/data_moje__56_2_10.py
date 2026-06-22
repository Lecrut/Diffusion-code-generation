def multiplication_table(n):
    for i in range(1, 11):
        yield n * i

if __name__ == '__main__':
    n = 5
    results = list(multiplication_table(n))
    print(results)