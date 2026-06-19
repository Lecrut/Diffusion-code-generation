def calculate_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    shape_data = {
        'triangle': {'base': 10, 'height': 5}
    }
    shape_type = 'triangle'
    result = calculate_area(shape_data[shape_type]['base'], shape_data[shape_type]['height'])
    print(result)