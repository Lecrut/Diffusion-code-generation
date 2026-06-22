def print_multiplication_table(n, start, end):
    for i in range(start, end + 1):
        print(f"{n} x {i} = {n * i}")

if __name__ == '__main__':
    print_multiplication_table(5, 1, 10)