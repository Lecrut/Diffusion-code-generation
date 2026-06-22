def print_multiplication_table_for_eight() -> None:
    multiplier: int = 1
    while multiplier <= 10:
        result: int = 8 * multiplier
        print(f"8 x {multiplier} = {result}")
        multiplier += 1

if __name__ == '__main__':
    print_multiplication_table_for_eight()