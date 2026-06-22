def generate_hollow_square_line(size):
    if size < 2:
        return ""
    
    line = "*" * size + "\n"
    for _ in range(size - 2):
        line += "*" + " " * (size - 2) + "*\n"
    line += "*" * size
    
    return line

if __name__ == '__main__':
    sample_size = 5
    print(generate_hollow_square_line(sample_size))