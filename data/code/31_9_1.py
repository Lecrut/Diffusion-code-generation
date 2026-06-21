def hex_to_int(hex_str):
    result = 0
    for char in hex_str.lower():
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        else:
            raise ValueError("Invalid hex character")
        result = result * 16 + value
    return result

if __name__ == '__main__':
    print(hex_to_int("1a3f"))
    print(hex_to_int("FF"))
    print(hex_to_int("0"))
    print(hex_to_int("deadBEEF"))