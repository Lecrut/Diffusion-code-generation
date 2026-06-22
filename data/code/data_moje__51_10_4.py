def generate_number_pyramid(height: int) -> str:
    lines = []
    for i in range(1, height + 1):
        numbers = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
        line = ' '.join((str(num) for num in numbers))
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    pyramid = generate_number_pyramid(5)
    print(pyramid)