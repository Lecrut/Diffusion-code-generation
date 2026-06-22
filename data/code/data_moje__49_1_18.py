def print_star_square(size):
    if size <= 0:
        return ""
    
    lines = []
    for i in range(size):
        if i == 0 or i == size - 1:
            line = "*" * size
        else:
            line = "*" + " " * (size - 2) + "*"
        lines.append(line)
    
    result = "\n".join(lines)
    print(result)
    return result

if __name__ == '__main__':
    print_star_square(5)