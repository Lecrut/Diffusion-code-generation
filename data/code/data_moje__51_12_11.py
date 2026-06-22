def generate_number_pyramid(size):
    lines = []
    for row in range(1, size + 1):
        spaces = ' ' * (size - row)
        numbers = ' '.join(str(num) for num in range(1, row + 1))
        lines.append(f"{spaces}{numbers}")
    return lines

if __name__ == '__main__':
    result = generate_number_pyramid(6)
    for line in result:
        print(line)