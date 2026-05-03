import time
import math
def calculate_rectangle_area(rectangles):
    total_area = 0
    for length, width in rectangles:
        total_area += length * width
    return total_area
def calculate_circle_area(circles):
    total_area = 0
    for radius in circles:
        total_area += math.pi * radius**2
    return total_area
NUM_ITEMS = 10000
rectangle_data = []
circle_data = []
for i in range(NUM_ITEMS):
    rectangle_data.append((float(i) + 1, float(i) + 2))
    circle_data.append(float(i) + 1.5)
start_time = time.perf_counter()
rectangle_result = calculate_rectangle_area(rectangle_data)
circle_result = calculate_circle_area(circle_data)
end_time = time.perf_counter()
print(f"Rectangle Area Calculation: {rectangle_result}")
print(f"Circle Area Calculation: {circle_result}")
print(f"Time taken for Rectangles: {end_time - start_time:.6f} seconds")
print(f"Time taken for Circles: {end_time - start_time:.6f} seconds")
if __name__ == '__main__':
    pass