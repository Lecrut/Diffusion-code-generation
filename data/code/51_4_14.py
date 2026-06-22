def generate_number_pyramid():
    lines = []
    for row in range(1, 4):
        line = " " * (3 - row)
        numbers = " ".join(str(x) for x in range(1, row + 1))
        lines.append(line + numbers + " " * (3 - row))
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_number_pyramid()
    print(result)