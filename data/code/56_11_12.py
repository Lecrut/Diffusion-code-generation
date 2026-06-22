def generate_multiplication_table(number: int, limit: int = 12) -> str:
    return "\n".join(f"{number} x {i} = {number * i}" for i in range(1, limit + 1))

if __name__ == "__main__":
    table_string = generate_multiplication_table(7)
    print(table_string)