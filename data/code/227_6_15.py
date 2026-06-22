def print_star_pyramid(height):
    if not isinstance(height, int) or height < 1:
        raise ValueError("Height must be a positive integer")
    
    for i in range(1, height + 1):
        row = " " * (height - i) + "* " * (2 * i - 1)
        print(row.strip())

if __name__ == '__main__':
    try:
        print_star_pyramid(3)
    except ValueError as e:
        print(e)