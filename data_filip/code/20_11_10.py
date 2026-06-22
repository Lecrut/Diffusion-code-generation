def run_length_encode(data: str) -> list[list]:
    if not data:
        return []
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append([current_char, count])
            current_char = char
            count = 1
    encoded.append([current_char, count])
    return encoded

if __name__ == '__main__':
    input_string = "1122233334"
    result = run_length_encode(input_string)
    print(result)