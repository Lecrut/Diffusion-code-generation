import time

def calculate_rectangle_area(w: float, h: float) -> float:
    """Calculate area of a single rectangle."""
    return w * h

def calculate_circle_area(r: float) -> float:
    """Calculate area of a single circle using pi approximation for speed comparison."""
    import math
    return math.pi * (r ** 2)

def benchmark_shapes(count: int = 10_000):
    # Generate sample dimensions without user input or files
    rectangle_widths = [i + 5.0 for i in range(count)]
    rectangle_heights = [j + 3.0 for j in range(count)]
    
    circle_radii = [(k * 1.2) for k in range(count)]

    # Initialize timing variables
    start_rect_time = time.perf_counter() if hasattr(time, 'perf_counter') else time.time()
    total_rectangle_area_sum = sum(calculate_rectangle_area(w, h) 
                                   for w, h in zip(rectangle_widths, rectangle_heights))
    
    end_rect_time = time.perf_counter() if hasattr(time, 'perf_counter') else time.time()

    start_circle_time = time.perf_counter() if hasattr(time, 'perf_counter') else time.time()
    total_circle_area_sum = sum(calculate_circle_area(r) for r in circle_radii)
    
    end_circle_time = time.perf_counter() if hasattr(time, 'perf_counter') else time.time()

    # Calculate elapsed times and performance metrics
    rectangle_elapsed_ms = (end_rect_time - start_rect_time) * 1000
    circle_elapsed_ms = (end_circle_time - start_circle_time) * 1000
    
    print(f"Shape Comparison Benchmark: {count} items")
    print("-" * 40)
    
    # Rectangle results
    rect_avg_area = total_rectangle_area_sum / count
    print(f"Rectangle Area Calculation:")
    print(f"  Average area per shape: {rect_avg_area:.2f}")
    print(f"  Total area for all shapes: {total_rectangle_area_sum:.2f}")
    print(f"  Execution time (approx): {rectangle_elapsed_ms:.4f} ms")

    # Circle results
    circle_avg_area = total_circle_area_sum / count
    print(f"\nCircle Area Calculation:")
    print(f"  Average area per shape: {circle_avg_area:.2f}")
    print(f"  Total area for all shapes: {total_circle_area_sum:.2f}")
    print(f"  Execution time (approx): {circle_elapsed_ms:.4f} ms")

    # Efficiency comparison logic
    if rectangle_elapsed_ms < circle_elapsed_ms:
        efficiency_ratio = circle_elapsed_ms / rectangle_elapsed_ms
        print(f"\nPerformance Analysis:")
        print(f"  Rectangles are faster than circles by a factor of {efficiency_ratio:.2x}")
        reason = "due to simpler arithmetic operations (multiplication only) vs floating point multiplication and power function."
    else:
        efficiency_ratio = rectangle_elapsed_ms / circle_elapsed_ms if circle_elapsed_ms > 0 else float('inf')
        print(f"\nPerformance Analysis:")
        print(f"  Circles are faster than rectangles by a factor of {efficiency_ratio:.2f}")
        reason = "likely due to optimized math library implementations for pi and power operations in CPython."

    print(f"  Note: The difference is often negligible at this scale because both involve O(1) per-item complexity.")
    if 'reason' not in dir():
        # Fallback message since the above conditional structure doesn't explicitly set a variable named 'reason' for direct access
        pass 
    else:
        print(f"  {reason}")

if __name__ == '__main__':
    benchmark_shapes()