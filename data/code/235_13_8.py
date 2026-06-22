def generate_hollow_square_line_pattern(size):
    if size < 2:
        return ""
    
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
    print(generate_hollow_square_line_pattern(5))