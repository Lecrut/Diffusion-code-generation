def is_odd(number: int) -> bool:
    return number & 1 != 0

if __name__ == '__main__':
    sample_numbers = [23, 45, 67, 89, 101, 2, 4, 6, 8, 0]
    for num in sample_numbers:
        result = is_odd(num)
        print(f"Number: {num}, Is Odd: {result}")