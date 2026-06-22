def generate_multiplication_table():
    lines = []
    for i in range(1, 13):
        row = ""
        for j in range(1, 13):
            product = i * j
            row += f"{j}x{i}={product:2}  "
        lines.append(row)
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_multiplication_table())