def validate_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if len(text) == 0:
        raise ValueError("Input string must not be empty")
    return True

def compress_string(text):
    validate_input(text)
    result = []
    current_char = text[0]
    count = 0
    for char in text:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return ''.join(result)

if __name__ == '__main__':
    sample = 'bbbaaa'
    output = compress_string(sample)
    print(output)