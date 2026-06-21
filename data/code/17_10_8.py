def run_length_encode(s: str) -> list:
    if not s:
        return []
    
    result = []
    iterator = iter(s)
    
    try:
        current_char = next(iterator)
        count = 1
    except StopIteration:
        return result
        
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    input_string = "AAABBC"
    encoded = run_length_encode(input_string)
    print(encoded)