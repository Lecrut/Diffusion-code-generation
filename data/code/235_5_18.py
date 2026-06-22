def print_triangle():
    max_value = 5
    for i in range(1, max_value + 1):
        spaces = ' ' * (max_value - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        pattern = spaces + numbers
        print(pattern)

if __name__ == '__main__':
    print_triangle()