import time
import math

def calculate_rectangle_areas(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given widths and heights."""
    if len(widths) != len(heights):
        raise ValueError("Widths and heights must be the same length.")
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_areas(radii: list[float]) -> float:
    """Calculate total area of circles given radii."""
    if not radii:
        return 0.0
    return math.pi * sum(r ** 2 for r in radii)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies.
    
    # Generate lists of length N = 10,000 with random floats between 1 and 5 (simulated).
    n_rectangles = 10_000
    
    widths = [math.random() * 4 + 1 for _ in range(n_rectangles)]
    heights = [math.random() * 4 + 1 for _ in range(n_rectangles)]
    
    radii = [math.random() * 2.5 + 0.5 for _ in range(n_rectangles)]

    # Benchmark rectangles
    rectangle_times = []
    iterations_rectangles = 3
    
    try:
        start_time = time.perf_counter_ns()
        
        for _ in range(iterations_rectangles):
            area_rectangles = calculate_rectangle_areas(widths, heights)
            
        end_time = time.perf_counter_ns()
        rectangle_total_time = (end_time - start_time) / 1_000_000_000
        
    except Exception as e:
        rectangle_total_time = None

    # Benchmark circles
    circle_times = []
    
    try:
        start_circle = time.perf_counter_ns()
        
        for _ in range(iterations_rectangles):
            area_circles = calculate_circle_areas(radii)
            
        end_circle = time.perf_counter_ns()
        circle_total_time = (end_circle - start_circle) / 1_000_000_000
        
    except Exception as e:
        circle_total_time = None

    if rectangle_times and not any(rect == float('inf') or rect == float('-inf') for rect in rectangle_times):
        avg_rect_time = sum(rectangle_times) / len(rectangle_times)
    else:
        print(f"Error calculating rectangles time. Reason might be {e}")
    
    if circle_times and not any(circle == float('inf') or circle == float('-inf') for circle in circle_times):
        avg_circle_time = sum(circle_times) / len(circle_times)
    else:
        print(f"Error calculating circles time. Reason might be {e}")

    # Print results
    if rectangle_total_time is not None and circle_total_time is not None:
        rect_avg_ns = (rectangle_total_time * 1_000_000_000) / iterations_rectangles
        circ_avg_ns = (circle_total_time * 1_000_000_000) / iterations_rectangles
        
        print(f"Number of shapes: {n_rectangles}")
        print(f"Average time for rectangles per run: {rect_avg_ns:.6f} nanoseconds")