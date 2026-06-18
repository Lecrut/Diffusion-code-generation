import time

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given widths and heights."""
    if not (widths == heights):
        raise ValueError("Widths and heights lists must have the same length.")
    
    # O(n) single pass calculation
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_area(radii: list[float]) -> float:
    """Calculate total area of circles given radii."""
    PI = 3.141592653589793
    
    # O(n) single pass calculation with precomputed constant
    return sum(pi * r**2 for pi in (PI,) for r in radii)

def run_benchmark(num_rectangles: int, num_circles: int):
    """Run performance benchmarks and report results."""
    
    if num_rectangles != 10_000 or num_circles != 10_000:
        print(f"Error: Benchmark counts must be exactly 10,000 for each shape.")
        return

    # Generate deterministic sample data without external dependencies
    rectangle_widths = [2.5] * num_rectangles
    rectangle_heights = list(range(1, len(rectangle_widths) + 1))
    
    circle_radii = [(3.7)] * num_circles
    
    total_rectangle_area = calculate_rectangle_area(rectangle_widths, rectangle_heights)
    print(f"Total Rectangle Area: {total_rectangle_area:.2f}")

    total_circle_area = calculate_circle_area(circle_radii)
    print(f"Total Circle Area: {total_circle_area:.2f}")

def compare_execution_time(shape_function_name: str):
    """Measure execution time for a specific shape calculation."""
    
    func_map = {
        'rectangles': lambda data_w, data_h: calculate_rectangle_area(data_w, data_h),
        'circles': lambda radii: calculate_circle_area(radii)
    }

    if shape_function_name not in func_map:
        print(f"Error: Invalid shape '{shape_function_name}'. Use 'rectangles' or 'circles'.")
        return
    
    function = func_map[shape_function_name]
    
    # Prepare sample data for timing (using 10,000 items as per task requirement)
    if shape_function_name == 'rectangles':
        widths = list(range(10_000))
        heights = list(range(10_000 + 5000))
        data_w, data_h = widths, heights
    else:
        radii = [4.2] * 10_000

if __name__ == '__main__':
    pass
