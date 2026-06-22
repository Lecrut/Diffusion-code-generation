def multiplication_table_generator(n):
    for i in range(1, 11):
        yield f"{n} x {i} = {n * i}"

if __name__ == '__main__':
    for row in multiplication_table_generator(5):
        print(row)