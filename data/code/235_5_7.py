def print_hypotenuse_triangle(max_value):
    for i in range(1, max_value + 1):
        spaces = ' ' * (max_value - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)

if __name__ == '__main__':
    sample_max_value = 6
    print_hypotenuse_triangle(sample_max_value)