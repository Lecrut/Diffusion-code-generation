def check_parity(number: int) -> bool:
    return (number & 1) != 0
if __name__ == '__main__':
    test_values = [5, 6, 7, 8]
    for val in test_values:
        result = check_parity(val)
        print(f"Parity of {val}: {result}")