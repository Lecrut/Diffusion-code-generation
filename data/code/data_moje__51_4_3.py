def generate_number_pyramid():
    lines = []
    row = 1
    while row <= 3:
        spaces = " " * (3 - row)
        line = spaces + (str(row) + " ") * row
        lines.append(line.rstrip())
        row += 1
    return "\n".join(lines)

if __name__ == "__main__":
    result = generate_number_pyramid()
    print(result)