def generate_number_pyramid(height: int=5) -> str:
    lines = []
    for row in range(1, height + 1):
        left_part = list(range(1, row + 1))
        right_part = list(range(row - 1, 0, -1))
        numbers = left_part + right_part
        line = ' '.join((str(num) for num in numbers))
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    print(generate_number_pyramid())