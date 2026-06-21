import time
RECTANGLE = 'rectangle'
CIRCLE = 'circle'

def calculate_area(shape_type, *dimensions):
    if shape_type == RECTANGLE:
        width, height = dimensions
        return width * height
    elif shape_type == CIRCLE:
        radius, = dimensions
        return 3.14159 * radius * radius
    else:
        raise ValueError('Unsupported shape type')

def benchmark_shapes(rectangles, circles):
    start_time = time.time()
    total_area = 0
    for width, height in rectangles:
        total_area += calculate_area(RECTANGLE, width, height)
    for radius in circles:
        total_area += calculate_area(CIRCLE, radius)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return (total_area, elapsed_time)
if __name__ == '__main__':
    rectangles = [(5, 3)] * 10000
    circles = [2] * 10000
    total_area, elapsed_time = benchmark_shapes(rectangles, circles)
    print(f'Total Area: {total_area}')
    print(f'Elapsed Time: {elapsed_time:.6f} seconds')