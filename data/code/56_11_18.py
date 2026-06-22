def generate_multiplication_table_7():
    lines = []
    for i in range(1, 11):
        lines.append(f"7 x {i} = {7 * i}")
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_multiplication_table_7())