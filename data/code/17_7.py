def get_number_and_parity(n: int) -> tuple[int, bool]:
    parity = n % 2 == 0
    return (n, parity)
if __name__ == '__main__':
    test_numbers = [1, 2, 3, 4, 5, 0, -2, -3]
    for number in test_numbers:
        result = get_number_and_parity(number)
        print(f"Input: {number}, Result: {result}")