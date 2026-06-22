def generate_number_pyramid():
    height = 5
    max_width = len(str(height * 10 + 5)) * height + (height - 1)
    result = []
    for row_num in range(1, height + 1):
        spaces = ' ' * (height - row_num)
        numbers = ' '.join(str(num) for num in range(1, row_num + 1))
        line = f"{spaces}{numbers}"
        result.append(line)
    print('\n'.join(result))

if __name__ == '__main__':
    generate_number_pyramid()