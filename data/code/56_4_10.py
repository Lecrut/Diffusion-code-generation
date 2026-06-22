def print_multiplication_table(n, start=1, end=10):
    for i in range(start, end + 1):
        print(f"{n} x {i} = {n * i}")

if __name__ == '__main__':
    print_multiplication_table(5)