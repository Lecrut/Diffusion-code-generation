def hex_to_int(hex_string):
    result = 0
    for char in hex_string:
        result *= 16
        if '0' <= char <= '9':
            result += ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            result += ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            result += ord(char) - ord('A') + 10
    return result

if __name__ == '__main__':
    print(hex_to_int("1A3"))
    print(hex_to_int("FF"))
    print(hex_to_int("0"))
    print(hex_to_int("deadBEEF"))