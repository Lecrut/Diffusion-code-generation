def generate_multiplication_table(number: int) -> list[str]:
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]

def main() -> None:
    result = generate_multiplication_table(5)
    for line in result:
        print(line)

if __name__ == '__main__':
    main()