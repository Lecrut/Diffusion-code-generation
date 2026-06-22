def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    
    lines = []
    border_line = "*" * size
    middle_line = "*" + " " * (size - 2) + "*"
    
    lines.append(border_line)
    
    for _ in range(size - 2):
        lines.append(middle_line)
        
    if size > 1:
        lines.append(border_line)
        
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_hollow_square(5))
    print(generate_hollow_square(1))
    print(generate_hollow_square(0))
    print(generate_hollow_square(3))