def hex_string_to_int(hex_str):
    result = 0
    length = len(hex_str)
    for i, char in enumerate(hex_str):
        if char.isupper():
            char = char.lower()
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        position = length - 1 - i
        result += value * (16 ** position)
    return result

if __name__ == '__main__':
    hex_input = "1a3f"
    integer_output = hex_string_to_int(hex_input)
    print(integer_output)