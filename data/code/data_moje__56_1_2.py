def generate_multiplication_table():
    max_value = 12
    table_rows = []
    for row in range(1, max_value + 1):
        row_values = []
        for col in range(1, max_value + 1):
            product = row * col
            formatted_value = f"{product:3d}"
            row_values.append(formatted_value)
        table_rows.append(" ".join(row_values))
    return "\n".join(table_rows)

if __name__ == "__main__":
    result = generate_multiplication_table()
    print(result)