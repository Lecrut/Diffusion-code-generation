def check_for_oddness(number: int) -> bool:
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    return number & 1 != 0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in sample_numbers:
        try:
            result = check_for_oddness(num)
            print(f"Number: {num}, Is Odd: {result}")
        except ValueError as e:
            print(e)