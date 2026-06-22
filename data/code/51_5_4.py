def build_hollow_pyramid(rows):
    if rows <= 0:
        return ""
    result = []
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        if i == 1:
            line = spaces + "*" + spaces
        elif i == rows:
            line = spaces + "*" + (" *" * (i - 1))
        else:
            line = spaces + "*" + (" " * (2 * i - 3)) + "*"
        result.append(line)
    return "\n".join(result)

if __name__ == '__main__':
    sample_rows = 5
    print(build_hollow_pyramid(sample_rows))