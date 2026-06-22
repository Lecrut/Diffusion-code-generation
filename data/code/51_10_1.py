def generate_number_pyramid(height=5):
    lines = []
    for i in range(1, height + 1):
        row_str = ' '.join(str(i) for _ in range(i))
        lines.append(row_str)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_number_pyramid()
    print(result)