def generate_pyramid(height):
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer.")
    
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        line = spaces + "+ " * i
        print(line)

if __name__ == '__main__':
    generate_pyramid(5)