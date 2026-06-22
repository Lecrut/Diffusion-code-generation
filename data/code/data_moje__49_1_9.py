def print_star_square(size):
    if size <= 0:
        return ""
    result = []
    for i in range(size):
        if i == 0 or i == size - 1:
            result.append('*' * size)
        else:
            result.append('*' + ' ' * (size - 2) + '*')
    return '\n'.join(result)

if __name__ == '__main__':
    print(print_star_square(5))
    print(print_star_square(3))
    print(print_star_square(1))
    print(print_star_square(4))