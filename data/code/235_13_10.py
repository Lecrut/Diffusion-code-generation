def generate_hollow_square_line_pattern(size):
    if not isinstance(size, int) or size < 1:
        raise ValueError("Size must be a positive integer")
    
    pattern = ""
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                pattern += "*"
            else:
                pattern += " "
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    try:
        print(generate_hollow_square_line_pattern(5))
    except ValueError as e:
        print(e)