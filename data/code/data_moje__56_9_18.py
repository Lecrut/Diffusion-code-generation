def calculate_multiplication_table(base: int, count: int) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    for i in range(1, count + 1):
        product: int = base * i
        result.append((base, i, product))
    return result

if __name__ == '__main__':
    table = calculate_multiplication_table(8, 12)
    for entry in table:
        print(f"{entry[0]} x {entry[1]} = {entry[2]}")