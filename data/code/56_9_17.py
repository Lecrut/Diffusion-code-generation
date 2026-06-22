def calculate_multiplication_table(value: int, limit: int = 10) -> list[int]:
    table: list[int] = [value * i for i in range(1, limit + 1)]
    for i, product in enumerate(table, start=1):
        print(f"{value} x {i} = {product}")
    return table

if __name__ == '__main__':
    result = calculate_multiplication_table(8)
    print(result)