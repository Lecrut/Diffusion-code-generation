def binary_to_hex(binary_strings):
    hex_list = []
    for binary in binary_strings:
        try:
            if not all(c in '01' for c in binary):
                raise ValueError("Invalid binary string: contains characters other than 0 and 1")
            decimal_value = int(binary, 2)
            hex_value = format(decimal_value, 'X')
            hex_list.append(hex_value)
        except ValueError as e:
            raise e
    return hex_list

if __name__ == '__main__':
    sample_data = ['0000', '0001', '1010', '1111', '10101', '21']
    try:
        result = binary_to_hex(sample_data)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")