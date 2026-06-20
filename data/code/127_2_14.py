def is_odd(number: int) -> bool:
    return number & 1 != 0

if __name__ == '__main__':
    test_numbers = [23, 44, 67, -89, 0]
    for num in test_numbers:
        result = is_odd(num)
        print(f"Number: {num}, Is Odd: {result}")