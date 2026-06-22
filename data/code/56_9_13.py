def generate_multiplication_table_8() -> list:
    table = []
    for i in range(1, 11):
        table.append(8 * i)
    return table

def main() -> None:
    results = generate_multiplication_table_8()
    for value in results:
        print(value)

if __name__ == '__main__':
    main()