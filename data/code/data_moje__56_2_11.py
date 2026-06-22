def multiplication_table_generator(n):
    for i in range(1, 11):
        yield f"{n} x {i} = {n * i}"

if __name__ == '__main__':
    number = 7
    for row in multiplication_table_generator(number):
        print(row)