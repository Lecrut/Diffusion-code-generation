def multiplication_table(n):
    i = 1
    while i <= 10:
        yield f"{n} x {i} = {n * i}"
        i += 1

if __name__ == '__main__':
    num = 5
    for row in multiplication_table(num):
        print(row)