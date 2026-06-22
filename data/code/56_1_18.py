def generate_multiplication_table():
    table_lines = []
    header = "   " + " ".join(f"{i:>4}" for i in range(1, 13))
    table_lines.append(header)
    for i in range(1, 13):
        row = f"{i:>2}" + " ".join(f"{i*j:>4}" for j in range(1, 13))
        table_lines.append(row)
    return "\n".join(table_lines)

if __name__ == '__main__':
    result = generate_multiplication_table()
    print(result)