def generate_centered_pyramid(height):
    result_lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        line = f"{spaces}{numbers}{spaces}"
        result_lines.append(line)
    return '\n'.join(result_lines)

if __name__ == '__main__':
    pyramid = generate_centered_pyramid(7)
    print(pyramid)