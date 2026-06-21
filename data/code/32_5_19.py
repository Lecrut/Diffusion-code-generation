def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric values.")
    return width * height

if __name__ == '__main__':
    w1 = 5
    h1 = 10
    print(calculate_rectangle_area(w1, h1))
    w2 = 7.5
    h2 = 4.2
    print(calculate_rectangle_area(w2, h2))
    try:
        print(calculate_rectangle_area("5", 10))
    except TypeError as e:
        print(e)