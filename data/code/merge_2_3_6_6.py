def check_parity(n: int) -> bool:
    return (n & 1) != 0
if __name__ == '__main__':
    sample_values = [7, 8, 9]
    for val in sample_values:
        parity_result = check_parity(val)
        print(f"Value {val}: Parity is {'odd' if parity_result else 'even'}")