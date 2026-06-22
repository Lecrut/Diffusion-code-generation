def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    
    lines = []
    for i in range(size):
        if i == 0 or i == size - 1:
            line = "*" * size
        else:
            line = "*" + " " * (size - 2) + "*"
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)