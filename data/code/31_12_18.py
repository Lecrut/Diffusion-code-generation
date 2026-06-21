def hex_to_decimal(hex_list):
    return [int(h, 16) for h in hex_list]

if __name__ == '__main__':
    hex_values = ['0x1A', '0xFF', '0x2B', '0x0', '0x123', '0xABCD', '0x10', '0xFFFFFFFF']
    print(hex_to_decimal(hex_values))