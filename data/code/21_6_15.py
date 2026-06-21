def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    current_char = data[0]
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode("aaabbc"))
    print(run_length_encode("xyz"))
    print(run_length_encode(""))
    print(run_length_encode("aaaa"))