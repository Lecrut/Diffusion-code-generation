def run_length_compress(char_list: list[str]) -> list[tuple[str, int]]:
    if not char_list:
        return []
    
    result = []
    current_char = char_list[0]
    count = 1
    
    for char in char_list[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
            
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'b', 'b', 'c']
    output = run_length_compress(sample_input)
    print(output)