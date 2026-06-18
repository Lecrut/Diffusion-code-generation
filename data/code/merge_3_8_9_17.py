import time
import math

def calculate_rectangle_area(widths, heights):
    """Calculate total area of rectangles given widths and heights."""
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_area(radiuses):
    """Calculate total area of circles given radii using pi*r^2."""
    return math.pi * sum(r ** 2 for r in radiuses)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input, args, or network access)
    
    num_rectangles = 10_000
    num_circles = 10_000
    
    # Generate random dimensions for rectangles and circles
    rects_widths = [math.random() * 10 + 1 for _ in range(num_rectangles)]
    rects_heights = [math.random() * 5 + 1 for _ in range(num_rectangles)]
    
    circle_radii = [math.random() * 2 + 1 for _ in range(num_circles)]
    
    # Time rectangle area calculation
    start_time = time.perf_counter_ns()
    result_rects = calculate_rectangle_area(rects_widths, rects_heights)
    end_time = time.perf_counter_ns()
    rect_elapsed_ms = (end_time - start_time) / 1_000_000
    
    # Time circle area calculation
    start_time = time.perf_counter_ns()
    result_circles = calculate_circle_area(circle_radii)
    end_time = time.perf_counter_ns()
    circle_elapsed_ms = (end_time - start_time) / 1_000_000
    
    # Output results for verification and comparison
    print(f"Rectangle Area Calculation:")
    print(f"Total area: {result_rects:.4f}")
    print(f"Elapsed time per rectangle count: {rect_elapsed_ms:.6f} ms")
    
    print("\nCircle Area Calculation:")
    print(f"Total area: {result_circles:.4f}")
    print(f"Elapsed time per circle count: {circle_elapsed_ms:.6f} ms")
    
    # Algorithmic efficiency comparison comment (explicitly allowed as documentation)
    """ 
    Performance Analysis Note:
    - Both algorithms perform O(n) operations where n is the number of shapes.
    - Rectangle calculation involves simple multiplication and accumulation.
    - Circle calculation requires squaring, floating-point multiplication with pi, and accumulation.
    - Floating-point arithmetic in Python generally has slight overhead compared to integer ops.
    - The circle algorithm typically shows marginally higher execution time due to:
      1. Additional mathematical operations (squaring) per element
      2. Use of the global math.pi constant lookup or multiplication factor
    """