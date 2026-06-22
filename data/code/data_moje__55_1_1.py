def print_centered_alphabet_triangle(height):
    if height <= 0:
        return []
    
    lines = []
    for i in range(height):
        num_chars = 2 * i + 1
        char = chr(65 + i)
        line = char * num_chars
        spaces = ' ' * (height - 1 - i)
        full_line = spaces + line + spaces
        lines.append(full_line)
    
    return lines

if __name__ == '__main__':
    result = print_centered_alphabet_triangle(5)
    for line in result:
        print(line)