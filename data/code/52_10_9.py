def generate_diamond_pattern(size):
    result = []
    half = (size - 1) // 2
    for i in range(size):
        if i <= half:
            spaces = ' ' * (half - i)
            stars = '*' * (2 * i + 1)
        else:
            spaces = ' ' * (i - half - 1)
            stars = '*' * (2 * (size - i - 1) - 1)
        line = spaces + stars + spaces
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_diamond_pattern(5))