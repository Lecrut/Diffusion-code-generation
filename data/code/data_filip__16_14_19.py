def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded_parts = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = run_length_encode(sample_input)
    print(result)
    
    empty_string = ""
    print(run_length_encode(empty_string))
    
    single_char = "A"
    print(run_length_encode(single_char))
    
    mixed_input = "AAABCCDDDD"
    print(run_length_encode(mixed_input))