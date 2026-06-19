triangle_area = lambda base, height: 0.5 * base * height

if __name__ == '__main__':
    dimensions = {'base': 14, 'height': 6}
    print(triangle_area(dimensions['base'], dimensions['height']))