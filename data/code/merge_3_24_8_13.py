def check_negative(value: int) -> None:
    """Prints a descriptive statement confirming if an integer is negative."""
    output = f"The number {value} {'is' if value < 0 else 'is not'} negative."
    print(output)

if __name__ == '__main__':
    sample_values = [-5, 10, -3]

    for num in sample_values:
        check_negative(num)