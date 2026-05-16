def calculate_area(shape, dimensions):
    if shape == 'square':
        side = dimensions
        return side * side
    elif shape == 'circle':
        radius = dimensions
        return 3.14159 * radius * radius
    elif shape == 'rectangle':
        length = dimensions[0]
        width = dimensions[1]
        return length * width
    else:
        return None
configuration = {
    'square': 'side',
    'circle': 'radius',
    'rectangle': 'dimensions'
}
sample_data = {
    'square': 5,
    'circle': 4,
    'rectangle': (10, 5)
}
results = {}
for shape, value in sample_data.items():
    if shape in configuration:
        key = configuration[shape]
        if shape == 'rectangle':
            dims = value
            area = calculate_area(shape, dims)
            results[shape] = area
        else:
            area = calculate_area(shape, value)
            results[shape] = area
if __name__ == '__main__':
    print(results)