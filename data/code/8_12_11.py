import math

def scaled_areas(shapes, scale_factor=1.0):
    return [
        {**shape, 'area': math.prod(shape.values()) * (scale_factor ** 2)}
        for shape in shapes
    ]

if __name__ == '__main__':
    data = [
        {'width': 2, 'height': 3},
        {'width': 4, 'height': 5},
        {'width': 1, 'height': 1}
    ]
    result = scaled_areas(data, scale_factor=2)
    print(result)