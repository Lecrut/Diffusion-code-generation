def print_triangle():
    for i in range(1, 6):
        spaces = ' ' * (5 - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)

if __name__ == '__main__':
    print_triangle()