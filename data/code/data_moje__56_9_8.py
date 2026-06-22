def calculate_multiplication_table() -> list[tuple[int, int, int]]:
    constant: int = 8
    table: list[tuple[int, int, int]] = []
    for i in range(1, 11):
        product: int = constant * i
        table.append((i, constant, product))
    return table

def print_multiplication_table() -> None:
    table: list[tuple[int, int, int]] = calculate_multiplication_table()
    for i, constant, product in table:
        print(f"{constant} x {i} = {product}")

if __name__ == '__main__':
    print_multiplication_table()