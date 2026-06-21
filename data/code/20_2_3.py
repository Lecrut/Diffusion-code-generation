def is_even(number: int) -> bool:
    return number % 2 == 0

if __name__ == "__main__":
    sample_values = [4, 7, 10, 13, 0, -2, -5]
    for value in sample_values:
        print(f"{value}: {is_even(value)}")