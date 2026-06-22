def generate_multiplication_table():
    header = f"{'':>4}"
    for i in range(1, 13):
        header += f"{i:>6}"
    print(header)
    print("-" * 43)
    for i in range(1, 13):
        row = f"{i:>4}"
        for j in range(1, 13):
            row += f"{i * j:>6}"
        print(row)

if __name__ == '__main__':
    generate_multiplication_table()