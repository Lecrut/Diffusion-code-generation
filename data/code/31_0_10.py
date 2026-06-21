def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_values = ['1A', 'FF', '10', 'ABCDEF']
    for value in sample_values:
        result = hex_to_decimal(value)
        print(result)