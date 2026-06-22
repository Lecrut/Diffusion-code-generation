def generate_number_pyramid(rows=6):
    result = []
    for i in range(1, rows + 1):
        center_line = " ".join(str(j) for j in range(1, i + 1))
        padding = " " * (rows - i)
        result.append(padding + center_line)
    return result

if __name__ == '__main__':
    pyramid_lines = generate_number_pyramid(6)
    for line in pyramid_lines:
        print(line)