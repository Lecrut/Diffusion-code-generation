import binascii

def binary_to_hexadecimal(binary_string: str) -> str:
    byte_length = (len(binary_string) + 7) // 8
    byte_array = bytearray(byte_length)
    for i in range(byte_length):
        start_index = i * 8
        end_index = start_index + 8
        byte_slice = binary_string[start_index:end_index]
        if len(byte_slice) < 8:
            byte_slice = byte_slice.zfill(8)
        byte_array[i] = int(byte_slice, 2)
    
    result_hex = binascii.hexlify(byte_array).decode('ascii')
    
    if len(binary_string) % 8 != 0:
        leading_bits = len(binary_string) % 8
        leading_value = int(binary_string[:leading_bits], 2)
        leading_hex_len = (leading_bits + 3) // 4
        result_hex = result_hex.lstrip('0') or '0'
        leading_hex_part = hex(leading_value)[2:].zfill(leading_hex_len)
        result_hex = leading_hex_part + result_hex[leading_hex_len:]
        
    return result_hex

if __name__ == '__main__':
    sample_binary = '11010100101010011110101110010110'
    result = binary_to_hexadecimal(sample_binary)
    print(result)