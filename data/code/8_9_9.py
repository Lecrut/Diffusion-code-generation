import time
import math

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given widths and heights."""
    if len(widths) != len(heights):
        raise ValueError("Widths and heights must have the same length.")
    
    # Algorithmic efficiency note: O(n) single pass is optimal for summing areas.
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_area(radii: list[float]) -> float:
    """Calculate total area of circles given radii."""
    # Algorithmic efficiency note: O(n) single pass is optimal here as well.
    # However, the constant factor involves a multiplication and square root per item.
    return sum(math.pi * r ** 2 for r in radii)

def benchmark_calculator(shape_func, data_list):
    """Run performance test on a given shape calculator."""
    start = time.perf_counter()
    result = shape_func(data_list)
    end = time.perf_counter()
    
    elapsed_time = end - start
    return result, elapsed_time

if __name__ == '__main__':
    # Hard-coded sample values for 10,000 items as per task requirement.
    n_items = 10_000
    
    # Generate random dimensions to simulate real-world data distribution.
    widths = [math.random() * 5 + 1 for _ in range(n_items)]
    heights = [math.random() * 3 + 2 for _ in range(n_items)]
    
    radii = [math.random() * 0.5 + 0.1 for _ in range(n_items)]

    # Benchmark rectangles
    rect_result, rect_time = benchmark_calculator(calculate_rectangle_area, widths)
    
    # Benchmark circles (using same count of items to ensure fair comparison)
    circle_result, circle_time = benchmark_calculator(calculate_circle_area, radii)
    
    print(f"Rectangle Area Calculation:")
    print(f"  Total Area: {rect_result:.2f}")
    print(f"  Time Taken: {rect_time*1000:.4f} ms")
    
    print("\nCircle Area Calculation:")
    print(f"  Total Area: {circle_result:.2f}")
    print(f"  Time Taken: {circle_time*1000:.4f} ms")
    
    # Simple efficiency comparison output
    if rect_time < circle_time:
        print("\nResult: Rectangle calculation was faster.")
    elif circle_time < rect_time:
        print("\nResult: Circle calculation was faster.")
    else:
        print("\nResult: Both calculations took approximately the same time.")