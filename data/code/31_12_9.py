def hex_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    data = ['1a', 'ff', '0', '100']
    result = hex_to_decimal(data)
    print(result)