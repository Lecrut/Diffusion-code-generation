def print_triangle():
    pattern = []
    for i in range(1, 6):
        spaces = ' ' * (5 - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        pattern.append(spaces + numbers)
    print('\n'.join(pattern))

if __name__ == '__main__':
    print_triangle()