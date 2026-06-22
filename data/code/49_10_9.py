def generate_square_pattern(side_length):
    lines = []
    for _ in range(side_length):
        lines.append("* " * side_length)
    return "\n".join(line.strip() for line in lines)

if __name__ == '__main__':
    result = generate_square_pattern(5)
    print(result)