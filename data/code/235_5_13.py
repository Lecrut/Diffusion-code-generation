MAX_VALUE = 5

def print_triangle():
    for i in range(1, MAX_VALUE + 1):
        spaces = ' ' * (MAX_VALUE - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)

if __name__ == '__main__':
    print_triangle()