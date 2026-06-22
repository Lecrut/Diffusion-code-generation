def generate_hollow_triangle(height=5):
    if height < 1:
        return ""
    rows = []
    for i in range(height):
        if i == 0:
            stars = "* " * height
            rows.append(stars.rstrip())
        elif i < height - 1:
            spaces = "  " * (i - 1)
            row = "* " + spaces + "* "
            rows.append(row.rstrip())
        else:
            stars = "* " * height
            rows.append(stars.rstrip())
    return "\n".join(rows)

if __name__ == '__main__':
    result = generate_hollow_triangle(5)
    print(result)