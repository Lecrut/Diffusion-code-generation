triangle_area = lambda base, height: 0.5 * base * height if base > 0 and height > 0 else None

if __name__ == '__main__':
    print(triangle_area(9, 6))