def check_parity(number: int) -> bool:
    return bool(number & 1)
if __name__ == '__main__':
    sample_values = [42, -7, 0, 1]
    for val in sample_values:
        result = check_parity(val)
        print(f"Parity of {val}: {'Even' if result else 'Odd'}")