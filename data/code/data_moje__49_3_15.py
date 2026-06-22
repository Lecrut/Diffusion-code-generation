def generate_star_square(size):
    if size < 1:
        return ""
    lines = []
    for i in range(size):
        if i == 0 or i == size - 1:
            lines.append('*' * size)
        else:
            lines.append('*' + ' ' * (size - 2) + '*')
    return '\n'.join(lines)

if __name__ == '__main__':
    size = 6
    result = generate_star_square(size)
    print(result)