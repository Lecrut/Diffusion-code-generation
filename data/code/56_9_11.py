def print_multiplication_table(value: int = 8) -> list[int]:
    result: list[int] = [value * i for i in range(1, 11)]
    for i in range(1, 11):
        print(f"{value} x {i} = {value * i}")
    return result

if __name__ == '__main__':
    print_multiplication_table()