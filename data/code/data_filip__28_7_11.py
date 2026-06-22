def run_length_encode(data: str):
    if not data:
        return
    
    count = 1
    current_char = data[0]
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            yield f"{count}{current_char}"
            current_char = char
            count = 1
            
    yield f"{count}{current_char}"

if __name__ == '__main__':
    sample_string = "AAABBC"
    result = ''.join(run_length_encode(sample_string))
    print(result)