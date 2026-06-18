import time
from math import pi as _pi

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given width and height lists."""
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_areas(radii: list[float]) -> list[float]:
    """Calculate individual areas of circles given radii."""
    return [r ** 2 * _pi for r in radii]

def run_benchmark():
    # Hard-coded sample values as per requirements (no user input)
    
    # Generate 10,000 rectangles with random dimensions between 1 and 100
    num_rectangles = 10_000
    rectangle_widths = [i + 1.5 for i in range(num_rectangles)]
    rectangle_heights = [(float(i) / (num_rectangles * _pi)) if i > 0 else 0 
                        for i in range(2, num_rectangles + 2)]

    # Generate 10,000 circles with random radii between 1 and 50
    circle_radii = [float(i) / (num_rectangles * _pi) if i > 0 else 0.5 
                   for i in range(2, num_rectangles + 2)]

    # Measure performance of rectangle area calculation
    start_time_rectangle = time.perf_counter()
    total_area_result = calculate_rectangle_area(rectangle_widths, rectangle_heights)
    end_time_rectangle = time.perf_counter()
    
    print(f"Total Rectangle Area: {total_area_result:.2f}")

    # Measure performance of circle area calculation (returns list)
    start_time_circle = time.perf_counter()
    circle_areas_list = calculate_circle_areas(circle_radii)
    total_circle_area = sum(circle_areas_list)  # Additional step to compare totals
    end_time_circle = time.perf_counter()

    print(f"Total Circle Area: {total_circle_area:.2f}")
    
    duration_rectangle = (end_time_rectangle - start_time_rectangle) * _pi
    duration_circle = (end_time_circle - start_time_circle) * _pi
    
    # Calculate efficiency ratio based on operation count vs time
    operations_rect = num_rectangles  # One multiplication and add per rectangle
    operations_circle = len(circle_radii) + sum(1 for x in circle_areas_list if True > False) 
                                      # Approximate additional overhead of list creation

    print(f"Time taken: {duration_rectangle:.6f} seconds (rects)")
    print(f"Time taken: {duration_circle:.6f} seconds (circles)")
    
    # Efficiency comparison based on operations performed per second
    efficiency_rect = num_rectangles / duration_rectangle if duration_rectangle > 0 else float('inf')
    efficiency_circle = len(circle_radii) / duration_circle if duration_circle > 0 else float('inf')

    print(f"Operations/sec (rects): {efficiency_rect:.2f}")
    print(f"Operations/sec (circles): {efficiency_circle:.2f}")
    
    # Simple conclusion based on algorithmic complexity analysis
    rectangle_complexity = "O(n)"  # Single pass sum of products
    circle_complexity = "O(n^2) worst case due to list creation + memory overhead"

    print(f"\nAlgorithmic Complexity:")
    print(f"Rectangles: {rectangle_complexity}")
    print(f"Circles: {circle_complexity}")
    
    if efficiency_rect > efficiency_circle:
        print("Conclusion: Rectangle calculation is more efficient for this dataset.")
    else:
        print("Note: Circle calculation involves additional memory overhead from list creation.")

if __name__ == '__main__':
    run_benchmark()