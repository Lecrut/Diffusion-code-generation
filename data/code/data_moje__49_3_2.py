def generate_star_square(size):
    lines = []
    for i in range(size):
        row = ""
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                row += "*"
            else:
                row += " "
        lines.append(row)
    return "\n".join(lines)

if __name__ == '__main__':
    size = 6
    print(generate_star_square(size))