def hex_to_int(hex_str):
    result = 0
    for char in hex_str:
        digit = ord(char) - ord('0')
        if digit < 0 or digit > 9:
            if ord('a') <= ord(char) <= ord('f'):
                digit = ord(char) - ord('a') + 10
            elif ord('A') <= ord(char) <= ord('F'):
                digit = ord(char) - ord('A') + 10
        result = result * 16 + digit
    return result

if __name__ == '__main__':
    print(hex_to_int("1A3"))
    print(hex_to_int("FF"))
    print(hex_to_int("0"))
    print(hex_to_int("deadBEEF"))