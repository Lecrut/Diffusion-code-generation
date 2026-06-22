def print_triangle(height):
    if height < 1:
        raise ValueError("Height must be at least 1")
    
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    height = 5
    print_triangle(height)