def generate_hollow_pyramid(rows):
    if rows <= 0:
        return ""
    lines = []
    for i in range(1, rows + 1):
        leading_spaces = " " * (rows - i)
        if i == 1:
            line = leading_spaces + str(i)
        elif i == rows:
            numbers = [str(i) for _ in range(2 * i - 1)]
            line = leading_spaces + "".join(numbers)
        else:
            first_num = str(i)
            last_num = str(i)
            middle_spaces = " " * (2 * (i - 1) - 1)
            line = leading_spaces + first_num + middle_spaces + last_num
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_hollow_pyramid(5)
    print(result)