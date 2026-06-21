import time

SHAPE_TYPES = {
    'rectangle': lambda width, height: width * height,
    'circle': lambda radius: 3.14159 * radius * radius
}

def calculate_area(shape_type, dimensions):
    return SHAPE_TYPES[shape_type](*dimensions)

def benchmark_shapes(rectangles, circles):
    start_time = time.time()
    
    total_area = 0
    for width, height in rectangles:
        total_area += calculate_area('rectangle', (width, height))
    
    for radius in circles:
        total_area += calculate_area('circle', (radius,))
    
    end_time = time.time()
    return total_area, end_time - start_time

if __name__ == '__main__':
    rectangles = [(10, 20)] * 10000
    circles = [5] * 10000
    
    total_area, elapsed_time = benchmark_shapes(rectangles, circles)
    
    print(f"Total Area: {total_area}")
    print(f"Elapsed Time: {elapsed_time} seconds")