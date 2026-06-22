def print_star_square(size):
    lines = []
    for i in range(size):
        if i == 0 or i == size - 1:
            lines.append('*' * size)
        else:
            lines.append('*' + ' ' * (size - 2) + '*')
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_star_square(6)
    print(result)