triangle_area = lambda base, height: 0.5 * base * height

if __name__ == '__main__':
    measurements = {'base': 14, 'height': 9}
    print(triangle_area(measurements['base'], measurements['height']))