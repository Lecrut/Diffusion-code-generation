def generate_number_pyramid():
    lines = []
    for row in range(1, 7):
        spaces = ' ' * (6 - row)
        numbers = ' '.join(str(num) for num in range(1, row + 1))
        lines.append(f"{spaces}{numbers}")
    return lines

if __name__ == '__main__':
    pyramid_lines = generate_number_pyramid()
    for line in pyramid_lines:
        print(line)