def check_parity(value):
    if not isinstance(value, int) or isinstance(value, bool):
        return "Error: Input must be an integer"
    if value % 2 == 0:
        return True
    return False

if __name__ == '__main__':
    sample_values = [4, 7, 0, -2, 3.5, "text", True, False]
    for val in sample_values:
        print(check_parity(val))