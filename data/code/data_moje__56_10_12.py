def print_multiplication_table(number: int, max_multiplier: int = 10) -> None:
    for i in range(1, max_multiplier + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    target_number = 5
    print_multiplication_table(target_number)