def check_parity(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer, got {type(n).__name__}")
    return n & 1 == 0
if __name__ == '__main__':
    sample_values = [42, -5, 0, 1]
    for val in sample_values:
        result = check_parity(val)
        print(f"Number {val}: Parity is {'Even' if result else 'Odd'}")