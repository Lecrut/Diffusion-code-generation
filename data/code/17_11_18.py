def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    encoded_parts: list[str] = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_data = "AAAABBBCCDAAAA"
    result = run_length_encode(sample_data)
    print(result)