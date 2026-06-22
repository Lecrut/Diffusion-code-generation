def generate_star_square(size):
    lines = []
    for i in range(size):
        line = ""
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                line += "*"
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    size = 6
    result = generate_star_square(size)
    print(result)