def generate_multiplication_table(number: int) -> list[str]:
    results: list[str] = []
    for i in range(1, 11):
        product: int = number * i
        results.append(f"{number} x {i} = {product}")
    return results

if __name__ == '__main__':
    values: list[str] = generate_multiplication_table(8)
    for line in values:
        print(line)