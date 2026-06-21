def run_length_encode(numeric_string: str) -> list:
    if not numeric_string:
        return []
    
    encoded = []
    count = 0
    current_char = numeric_string[0]
    
    for char in numeric_string:
        if char == current_char:
            count += 1
        else:
            encoded.append((count, current_char))
            count = 1
            current_char = char
    encoded.append((count, current_char))
    return encoded

if __name__ == '__main__':
    data = run_length_encode("11223")
    print(data)