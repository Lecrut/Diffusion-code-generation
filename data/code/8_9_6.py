import time
import math

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given widths and heights."""
    if not (widths == heights):
        raise ValueError("Widths and heights lists must be identical in length.")
    
    # Algorithmic efficiency note: 
    # This uses a generator expression to avoid creating an intermediate list,
    # which is O(n) time complexity with minimal memory overhead.
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_area(radii: list[float]) -> float:
    """Calculate total area of circles given radii."""
    if not radii:
        raise ValueError("Radii list cannot be empty.")
    
    # Algorithmic efficiency note: 
    # Using a generator expression here as well to maintain consistency.
    # The math.pi lookup is cached by Python, so the overhead per call is negligible compared to float multiplication.
    return sum(math.pi * r ** 2 for r in radii)

def benchmark_calculator(iterations: int = 10_000):
    """Run benchmarks comparing rectangle and circle area calculations."""
    
    # Generate sample data deterministically based on iteration count
    num_rectangles = iterations
    num_circles = iterations
    
    widths = [math.random() * 5.0 for _ in range(num_rectangles)]
    heights = list(widths)  # Ensure identical length as required by logic
    radii = [math.random() * 2.0 for _ in range(num_circles)]

    print(f"Starting benchmark with {num_rectangles} rectangles and {num_circles} circles...")

    start_time = time.perf_counter_ns()
    
    # Benchmark Rectangles
    rectangle_area_total = calculate_rectangle_area(widths, heights)
    
    end_time = time.perf_counter_ns()
    duration_rectangles_ms = (end_time - start_time) / 1_000_000.0
    
    print(f"Rectangle Area Total: {rectangle_area_total:.2f}")

    # Benchmark Circles
    circle_area_total = calculate_circle_area(radii)
    
    end_time_circles = time.perf_counter_ns()
    duration_circles_ms = (end_time_circles - start_time) / 1_000_000.0
    
    print(f"Circle Area Total: {circle_area_total:.2f}")

    # Performance comparison logic
    speedup_factor = duration_rectangles_ms / duration_circles_ms if duration_circles_ms > 0 else float('inf')
    
    if speedup_factor < 1 and speedup_factor != float('inf'):
        print(f"Circle calculation was {speedup_factor:.4f}x faster than rectangle calculation.")
    elif speedup_factor >= 1:
        print(f"Rectangle calculation was {speedup_factor - 1:.4f}x slower (or equal) compared to circle calculation.")

if __name__ == '__main__':
    # Hard-coded sample values logic is embedded in the function call above.
    # No external inputs, files, or network access are used.
    benchmark_calculator(iterations=10_000)