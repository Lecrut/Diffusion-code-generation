def check_parity(number: int) -> bool:
    return bool(number & 1)
if __name__ == '__main__':
    sample_values = [42, -5, 0, 7]
    for val in sample_values:
        result = check_parity(val)
        print(f"Number {val} is {'even' if result else 'odd'}")