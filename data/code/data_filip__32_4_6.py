def binary_to_hex(binary_str):
    for char in binary_str:
        if char not in ('0', '1'):
            raise ValueError(f"Invalid binary character: {char}")
    decimal_value = int(binary_str, 2)
    return hex(decimal_value)

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('11110000'))
    print(binary_to_hex('0'))
    try:
        print(binary_to_hex('1020'))
    except ValueError as e:
        print(e)