def generate_number_pyramid(rows):
    pyramid = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(num) for num in range(1, i + 1))
        line = f"{spaces}{numbers}"
        pyramid.append(line)
    return pyramid

if __name__ == '__main__':
    result = generate_number_pyramid(5)
    for line in result:
        print(line)