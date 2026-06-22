def encode_repeated_elements(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    print(encode_repeated_elements("aaabbc"))