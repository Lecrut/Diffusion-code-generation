import operator

def calculate_area(base, height):
    return operator.mul(base, height)

if __name__ == '__main__':
    dimensions = {'base': 8, 'height': 4}
    computed_area = calculate_area(dimensions['base'], dimensions['height'])
    print(computed_area)