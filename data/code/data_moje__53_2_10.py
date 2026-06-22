def reverse_number_triangle(height):
    result = []
    for row in range(height, 0, -1):
        line = ""
        for col in range(1, row + 1):
            line += str(col)
        result.append(line)
    return result

if __name__ == '__main__':
    height = 6
    lines = reverse_number_triangle(height)
    for line in lines:
        print(line)