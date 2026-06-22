def multiplication_table_8() -> list[str]:
    results: list[str] = []
    for i in range(1, 11):
        product = 8 * i
        results.append(f"8 x {i} = {product}")
    return results

if __name__ == '__main__':
    output = multiplication_table_8()
    for line in output:
        print(line)