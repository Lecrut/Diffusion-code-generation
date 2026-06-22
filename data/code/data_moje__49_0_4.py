def print_square_pattern(side_length):
    lines = []
    for i in range(side_length):
        line = ""
        for j in range(side_length):
            line += "*"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = print_square_pattern(5)
    print(result)