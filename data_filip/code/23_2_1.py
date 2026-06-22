def run_length_encode(input_string):
    if not input_string:
        return ""

    result = []
    count = 1
    current_char = input_string[0]

    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1

    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(input_string):
    if not input_string:
        return ""

    result = []
    count_str = ""

    for char in input_string:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str)
            result.append(char * count)
            count_str = ""

    return "".join(result)

if __name__ == '__main__':
    original = "AAABBC"
    encoded = run_length_encode(original)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)