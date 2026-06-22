def calculate_multiplication_table() -> list[str]:
    result: list[str] = []
    for i in range(1, 11):
        product: int = 8 * i
        result.append(f"{8} x {i} = {product}")
    return result

if __name__ == '__main__':
    table: list[str] = calculate_multiplication_table()
    for line in table:
        print(line)