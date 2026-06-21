def hex_string_to_integer(hex_str):
    if not hex_str:
        return 0
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    if hex_str.startswith('-') and (hex_str[2:].startswith('0x') or hex_str[2:].startswith('0X')):
        hex_str = hex_str[1:]
        return -int(hex_str, 16)
    if hex_str.startswith('-'):
        value = int(hex_str[1:], 16)
        return -value
    return int(hex_str, 16)

if __name__ == '__main__':
    samples = ["FF", "0xFF", "ff", "10", "0", "-FF"]
    for sample in samples:
        result = hex_string_to_integer(sample)
        print(result)