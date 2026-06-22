def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    iterator = iter(data)
    try:
        current_char = next(iterator)
    except StopIteration:
        return ""
    
    count = 1
    result_parts = []
    
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result_parts.append(f"{current_char}{count}")
    return "".join(result_parts)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCCDDDEEEEFFFF"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)