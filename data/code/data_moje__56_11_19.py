def generate_seven_multiplication_table() -> str:
    lines = [f"7 x {i} = {7 * i}" for i in range(1, 11)]
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_seven_multiplication_table())