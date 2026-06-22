def hex_to_int(hex_string: str) -> int:
    try:
        if not isinstance(hex_string, str):
            raise TypeError("Input must be a string")
        if hex_string.startswith(('0x', '0X')):
            return int(hex_string, 16)
        return int(hex_string, 16)
    except (ValueError, TypeError):
        return 0

if __name__ == '__main__':
    test_cases = ['0x1A', '0XFF', '0x0', '0xdeadBEEF', 'invalid', '', '0xGHI']
    for case in test_cases:
        print(hex_to_int(case))