import math
def calculate_area(shape, dimensions):
    if shape == 'square':
        side = dimensions
        return side * side
    elif shape == 'circle':
        radius = dimensions
        return math.pi * (radius ** 2)
    elif shape == 'rectangle':
        length = dimensions[0]
        width = dimensions[1]
        return length * width
    else:
        raise ValueError("Unknown shape")
if __name__ == '__main__':
    configurations = {
        'square': {'side': 5},
        'circle': {'radius': 4},
        'rectangle': {'length': 10, 'width': 3}
    }
    test_cases = [
        ('square', configurations['square']),
        ('circle', configurations['circle']),
        ('rectangle', configurations['rectangle'])
    ]
    for shape, dims in test_cases:
        try:
            area = calculate_area(shape, dims)
            print(f"Shape: {shape}, Dimensions: {dims}, Area: {area}")
        except ValueError as e:
            print(f"Error calculating area for {shape}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {shape}: {e}")