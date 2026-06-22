def generate_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ''.join(str(x) for x in range(1, i + 1))
        lines.append(f"{spaces}{numbers}")
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_height = 7
    result = generate_pyramid(sample_height)
    print(result)