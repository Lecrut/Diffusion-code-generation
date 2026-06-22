def generate_number_pyramid(height):
    pyramid_lines = []
    for i in range(1, height + 1):
        number = i
        line = ' ' * (height - i) + str(number) * i
        pyramid_lines.append(line)
    return '\n'.join(pyramid_lines)

if __name__ == '__main__':
    print(generate_number_pyramid(5))