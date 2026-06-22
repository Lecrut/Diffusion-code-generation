def generate_reverse_triangle(height: int) -> str:
    lines = []
    for i in range(height, 0, -1):
        lines.append(' ' * (height - i) + '* ' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_height = 4
    result = generate_reverse_triangle(sample_height)
    print(result)