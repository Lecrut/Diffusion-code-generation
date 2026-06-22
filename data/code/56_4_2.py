def print_multiplication_table(number: int, start: int = 1, end: int = 10) -> None:
    for i in range(start, end + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == '__main__':
    print_multiplication_table(5, 1, 10)