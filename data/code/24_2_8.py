def rle_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def rle_decode(input_string: str) -> str:
    result = []
    count = 0
    
    for char in input_string:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            result.append(char * count)
            count = 0
    
    return "".join(result)

if __name__ == '__main__':
    original = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = rle_encode(original)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded == original)