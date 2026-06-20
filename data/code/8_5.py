def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        length = dimensions[0]
        width = dimensions[1]
        return length * width
    elif shape == 'circle':
        radius = dimensions[0]
        return 3.14159 * radius * radius
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    sample_shapes = ['rectangle', 'circle']
    sample_dimensions = [
        [5, 10],
        [7]
    ]
    for i in range(len(sample_shapes)):
        shape = sample_shapes[i]
        dimensions = sample_dimensions[i]
        result = calculate_area(shape, dimensions)
        print(f"Area of {shape} with dimensions {dimensions} is {result}")