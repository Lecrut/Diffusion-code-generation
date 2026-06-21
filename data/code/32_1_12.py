def get_area(width, height):
    if width <= 0 or height <= 0:
        return 0.0
    return float(width * height)

if __name__ == '__main__':
    result = get_area(4.5, 2.0)
    print(result)