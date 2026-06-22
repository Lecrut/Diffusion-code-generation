def get_multiplication_table_for_eight() -> list[str]:
    results = []
    for i in range(1, 11):
        results.append(f"8 x {i} = {8 * i}")
    return results

if __name__ == '__main__':
    table = get_multiplication_table_for_eight()
    for line in table:
        print(line)