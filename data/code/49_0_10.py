def print_square(size):
    lines = []
    for i in range(size):
        row = ""
        for j in range(size):
            row += "*"
        lines.append(row)
    return "\n".join(lines)

if __name__ == '__main__':
    result = print_square(5)
    print(result)