def generate_hollow_square_line(size):
    if size < 2:
        return ""
    
    line = "+" + "-" * (size - 2) + "+\n"
    for _ in range(size - 2):
        line += "|" + " " * (size - 2) + "|\n"
    line += "+" + "-" * (size - 2) + "+"
    
    return line

if __name__ == '__main__':
    print(generate_hollow_square_line(5))