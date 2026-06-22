def generate_hollow_square(size: int, char: str) -> str:
    if size <= 0:
        return ""
    if size == 1:
        return char + "\n"
    
    line_top = char * size + "\n"
    line_middle = char + " " * (size - 2) + char + "\n"
    line_bottom = char * size
    
    result = [line_top]
    for _ in range(size - 2):
        result.append(line_middle)
    result.append(line_bottom)
    
    return "".join(result)

if __name__ == '__main__':
    side_length = 5
    square_string = generate_hollow_square(side_length, 'X')
    print(square_string)