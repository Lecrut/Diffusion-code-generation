def generate_multiplication_rows(n):
    for i in range(1, 11):
        yield f"{n} x {i} = {n * i}"

if __name__ == '__main__':
    for row in generate_multiplication_rows(9):
        print(row)