def generate_number_pyramid(height=5):
    lines = []
    for i in range(1, height + 1):
        number_part = str(i) * i
        line = number_part.center(height * 2 - 1)
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    pyramid = generate_number_pyramid(5)
    print(pyramid)