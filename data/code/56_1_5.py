def generate_multiplication_table():
    rows = []
    for i in range(1, 13):
        row = []
        for j in range(1, 13):
            row.append(f"{i * j:3}")
        rows.append(" ".join(row))
    return "\n".join(rows)

if __name__ == '__main__':
    print(generate_multiplication_table())