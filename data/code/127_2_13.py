ODD_CHECK_MASK = 1

def is_odd(number: int) -> bool:
    return (number & ODD_CHECK_MASK) != 0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in sample_numbers:
        result = is_odd(num)
        print(f"Number: {num}, Is Odd: {result}")