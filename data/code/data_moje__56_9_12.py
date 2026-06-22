def print_multiplication_table_8() -> None:
    i: int = 1
    while i <= 10:
        result: int = 8 * i
        print(f"{8} x {i} = {result}")
        i += 1

if __name__ == '__main__':
    print_multiplication_table_8()