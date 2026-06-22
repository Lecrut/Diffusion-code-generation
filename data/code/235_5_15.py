def print_triangle():
    max_value = 5
    if not isinstance(max_value, int) or max_value < 1:
        raise ValueError("max_value must be a positive integer")
    
    for i in range(1, max_value + 1):
        spaces = ' ' * (max_value - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)

if __name__ == '__main__':
    try:
        print_triangle()
    except ValueError as e:
        print(e)