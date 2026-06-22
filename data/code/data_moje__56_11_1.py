def generate_multiplication_table(number: int, limit: int = 10) -> str:
    lines = [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]
    return "\n".join(lines)

if __name__ == "__main__":
    result = generate_multiplication_table(7)
    print(result)