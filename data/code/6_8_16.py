STRING_CONST = " "
TARGET_CHAR = "_"

def _validate_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return True

def swap_spaces_for_underscores(text):
    _validate_input(text)
    chars = []
    for char in text:
        if char == STRING_CONST:
            chars.append(TARGET_CHAR)
        else:
            chars.append(char)
    return "".join(chars)

if __name__ == '__main__':
    input_data = "Python   is    powerful     and flexible"
    output_data = swap_spaces_for_underscores(input_data)
    print(output_data)