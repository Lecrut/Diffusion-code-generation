triangle_area = lambda base, height: (lambda b, h: 0.5 * b * h)(base, height) if base > 0 and height > 0 else "Invalid dimensions"

if __name__ == '__main__':
    print(triangle_area(10, 5))