def generate_multiplication_table(max_num=12):
    table = []
    for i in range(1, max_num + 1):
        row = []
        for j in range(1, max_num + 1):
            row.append(f"{i * j:4d}")
        table.append(" ".join(row))
    return "\n".join(table)

if __name__ == '__main__':
    print(generate_multiplication_table())