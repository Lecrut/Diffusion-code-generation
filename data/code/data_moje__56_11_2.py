def generate_seven_multiplication_table() -> str:
    lines = []
    for i in range(1, 11):
        lines.append(f"7 x {i} = {7 * i}")
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_seven_multiplication_table()
    print(result)