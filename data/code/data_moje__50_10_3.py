def print_right_angle_triangle(height):
    result = []
    for i in range(1, height + 1):
        row = '*' * i
        result.append(row)
    for line in result:
        print(line)
    return result

if __name__ == '__main__':
    height = 5
    lines = print_right_angle_triangle(height)
    print(lines)