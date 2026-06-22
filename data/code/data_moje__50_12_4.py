def hollow_equilateral_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        if i == 1:
            result.append(spaces + "*")
        elif i == rows:
            result.append(spaces + "*" + "* " * (rows - 1))
        else:
            result.append(spaces + "*" + " " * (2 * i - 3) + "*")
    return "\n".join(result)

if __name__ == '__main__':
    sample_rows = 5
    print(hollow_equilateral_triangle(sample_rows))