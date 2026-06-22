def hex_to_decimal(hex_string):
    return int(hex_string, 16)
if __name__ == '__main__':
    sample_values = ['1a', 'FF', '10', '2B5F', '0']
    for val in sample_values:
        print(hex_to_decimal(val))