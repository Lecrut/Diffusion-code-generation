def print_star_square(size):
    if size <= 0:
        return ""
    
    if size == 1:
        return "*"
    
    lines = []
    lines.append("*" * size)
    
    if size > 1:
        inner_space = " " * (size - 2)
        for _ in range(size - 2):
            lines.append("*" + inner_space + "*")
    
    lines.append("*" * size)
    
    for line in lines:
        print(line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    result = print_star_square(5)
    print("Returned string:", result)