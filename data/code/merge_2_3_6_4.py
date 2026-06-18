def check_parity(value: int) -> bool:
    return (value & 1) != 0
if __name__ == '__main__':
    sample_values = [5, 6, 7, -3]
    for val in sample_values:
        is_odd = check_parity(val)
        print(f"Value {val}: Parity (odd={is_odd})")