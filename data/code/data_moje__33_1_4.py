def triangle_area(base, height):
    if base <= 0 or height <= 0:
        return 0.0
    return base * height * 0.5

if __name__ == '__main__':
    b = 12.0
    h = 6.0
    print(triangle_area(b, h))