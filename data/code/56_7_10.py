def format_multiplication_table(base_number, table_size):
    width = max(len(str(base_number * table_size)), 4)
    rows = []
    for i in range(1, table_size + 1):
        product = base_number * i
        row = f"{base_number} x {i:<{width - len(str(i))}} = {product:<{width}}".rstrip()
        rows.append(row)
    return "\n".join(rows)

if __name__ == '__main__':
    print(format_multiplication_table(7, 10))