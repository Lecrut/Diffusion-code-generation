import time

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given widths and heights."""
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_area(radii: list[float]) -> float:
    """Calculate total area of circles given radii using pi = 3.141592653589793."""
    import math
    return sum(math.pi * r ** 2 for r in radii)

def benchmark_function(func, data_list):
    """Run a function on the provided list and measure execution time."""
    start = time.perf_counter()
    result = func(data_list)
    end = time.perf_counter()
    return result, (end - start) * 1_000_000

if __name__ == '__main__':
    # Hard-coded sample values for benchmarking without user input or files
    
    num_rectangles = 10_000
    num_circles = 10_000
    
    # Generate random dimensions (simulating real-world data)
    widths = [float(i * 2 + 3.5) for i in range(num_rectangles)]
    heights = [float(j * 4 + 7.2) for j in range(num_rectangles)]
    
    radii = [float(k / 10.5 - 0.8) if k % 3 != 0 else float((k // 3) * 0.9 + 1.1) 
             for k in range(num_circles)]

    # Ensure all values are positive to avoid mathematical errors
    widths = [max(0, w) for w in widths]
    heights = [max(0, h) for h in heights]
    radii = [abs(r) if r < 0 else r for r in radii]

    # Run benchmarks with warm-up simulation (implicit by direct execution)
    
    rect_result_rect_time = benchmark_function(calculate_rectangle_area, widths)
    circle_result_circle_time = benchmark_function(calculate_circle_area, radii)
    
    print(f"Rectangle Area: {rect_result_rect_time[0]:.2f}")
    print(f"Circle Area: {circle_result_circle_time[0]:.2f}")
    print(f"Time taken for Rectangles (us): {rect_result_rect_time[1]}")
    print(f"Time taken for Circles (us): {circle_result_circle_time[1]}")
    
    # Efficiency comparison logic based on algorithmic complexity O(n) vs O(n log n) if sorting was involved, 
    # but here both are strictly linear O(n). The difference lies in constant factors.