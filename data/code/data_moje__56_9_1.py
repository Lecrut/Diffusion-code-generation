def calculate_and_print_multiplication_table() -> None:
    constant_value = 8
    for multiplier in range(1, 11):
        result = constant_value * multiplier
        print(f"{constant_value} x {multiplier} = {result}")

if __name__ == "__main__":
    calculate_and_print_multiplication_table()