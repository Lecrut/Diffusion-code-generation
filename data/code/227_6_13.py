def print_star_pyramid(height):
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "* " * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    try:
        print_star_pyramid(3)
    except ValueError as e:
        print(e)