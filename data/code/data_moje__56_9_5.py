def print_multiplication_table(n: int) -> None:
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == '__main__':
    print_multiplication_table(8)