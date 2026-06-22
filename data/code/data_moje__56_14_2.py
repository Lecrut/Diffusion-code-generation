def generate_multiplication_table(number: int, size: int = 10) -> list[str]:
    return [f"{number} x {i} = {number * i}" for i in range(1, size + 1)]

if __name__ == '__main__':
    table = generate_multiplication_table(4)
    for line in table:
        print(line)