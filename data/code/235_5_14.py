def print_hypotenuse_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)

if __name__ == '__main__':
    print_hypotenuse_triangle(5)