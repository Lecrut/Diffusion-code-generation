def create_hollow_equilateral_triangle(height):
    if height < 1:
        return ""
    if height == 1:
        return "*"
    if height == 2:
        return "* *\n**"
    result = []
    for row in range(1, height + 1):
        spaces = ' ' * (height - row)
        if row == 1:
            result.append(f"{spaces}*")
        elif row == height:
            result.append(f"{spaces}{'* ' * row}")
        else:
            middle = '  ' * (row - 2)
            result.append(f"{spaces}*{middle}*")
    return '\n'.join(result)

if __name__ == '__main__':
    sample_height = 5
    print(create_hollow_equilateral_triangle(sample_height))