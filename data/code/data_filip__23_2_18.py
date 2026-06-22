def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

def run_length_decode(encoded_data: str) -> str:
    result = []
    count = 0
    for char in encoded_data:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            result.append(char * count)
            count = 0
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_output = run_length_encode(sample_input)
    decoded_output = run_length_decode(encoded_output)
    print(encoded_output)
    print(decoded_output)