import binascii

def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    if not all(c in '01' for c in binary_string):
        raise ValueError("Input must contain only binary digits (0 and 1)")
    decimal_value = int(binary_string, 2)
    hex_string = format(decimal_value, 'x')
    return hex_string

if __name__ == '__main__':
    test_cases = ["0", "1", "10", "1111", "10101010", "1111000011110000"]
    results = [binary_to_hex(case) for case in test_cases]
    for case, res in zip(test_cases, results):
        print(f"{case} -> {res}")