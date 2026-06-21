def run_length_encode(data):
    if data is None:
        raise TypeError("Input cannot be None")
    
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode("aaabbc"))
    print(run_length_encode(""))
    print(run_length_encode("abcdef"))