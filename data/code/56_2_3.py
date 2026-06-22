def multiplication_table(n):
    for i in range(1, 11):
        yield f"{n} x {i} = {n * i}"

if __name__ == '__main__':
    for row in multiplication_table(5):
        print(row)