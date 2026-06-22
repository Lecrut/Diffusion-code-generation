def print_pyramid(height):
    if height < 1:
        raise ValueError("Height must be at least 1")
    
    max_width = 2 * height - 1
    
    for i in range(1, height + 1):
        spaces = " " * (max_width // 2 - i + 1)
        plus_signs = "+" * (2 * i - 1)
        print(spaces + plus_signs)

if __name__ == '__main__':
    HEIGHT = 5
    print_pyramid(HEIGHT)