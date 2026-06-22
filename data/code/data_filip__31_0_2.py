def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    test_values = ['1A', 'FF', '100', 'ABCDEF']
    for value in test_values:
        result = hex_to_decimal(value)
        print(f"{value} -> {result}")