def calculate_rectangle_area(width, height):
    if width < 0:
        raise ValueError("Width cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return width * height

if __name__ == '__main__':
    width = 5
    height = 10
    print(calculate_rectangle_area(width, height))