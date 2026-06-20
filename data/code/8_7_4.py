import time
import math

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def benchmark_calculations():
    iterations = 10000
    rectangle_data = [(5, 10) for _ in range(iterations)]
    circle_data = [7 for _ in range(iterations)]
    
    start_time = time.perf_counter()
    rect_results = [calculate_rectangle_area(w, h) for w, h in rectangle_data]
    end_time = time.perf_counter()
    rect_duration = end_time - start_time
    
    start_time = time.perf_counter()
    circ_results = [calculate_circle_area(r) for r in circle_data]
    end_time = time.perf_counter()
    circ_duration = end_time - start_time
    
    return rect_duration, circ_duration, rect_results[-1], circ_results[-1]

if __name__ == '__main__':
    rect_time, circ_time, last_rect_area, last_circ_area = benchmark_calculations()
    print(last_rect_area)
    print(last_circ_area)
    print(rect_time)
    print(circ_time)