def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_1 = '0x1A3F'
    sample_2 = 'FF'
    sample_3 = '0xdeadbeef'
    print(hex_to_decimal(sample_1))
    print(hex_to_decimal(sample_2))
    print(hex_to_decimal(sample_3))