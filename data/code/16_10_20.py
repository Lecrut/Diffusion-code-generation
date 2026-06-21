def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""

    result = []
    count = 1
    prev_char = input_string[0]

    for char in input_string[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            prev_char = char
            count = 1
    
    result.append(f"{count}{prev_char}")
    
    return "".join(result)

def run_length_decode(input_string: str) -> str:
    if not input_string:
        return ""

    result = []
    count_str = []
    
    for char in input_string:
        if char.isdigit():
            count_str.append(char)
        else:
            count = int("".join(count_str))
            result.append(char * count)
            count_str = []
            
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBC"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    
    print(f"Original: {original}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")