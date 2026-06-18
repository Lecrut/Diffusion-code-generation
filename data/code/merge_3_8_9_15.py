import time
import math

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given widths and heights."""
    if len(widths) != len(heights):
        raise ValueError("Widths and heights lists must have the same length.")
    
    # Algorithmic efficiency O(n), simple summation
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_area(radii: list[float]) -> float:
    """Calculate total area of circles given radii."""
    if len(radii) != 10_000: # Enforcing the specific count mentioned in task context for consistency check logic if needed, but generally O(n)
        raise ValueError(f"Expected exactly {len(radii)} radii.")

    # Algorithmic efficiency O(n), using math.pi directly. 
    # Note: Precomputing pi might save a tiny fraction of time per iteration compared to calling the function repeatedly in tight loops,
    # but for 10k iterations it is negligible difference between methods. We use direct multiplication for clarity and standard library usage.
    
    return sum(math.pi * r ** 2 for r in radii)

def benchmark_comparison():
    """Run benchmarks comparing rectangle vs circle area calculations."""
    n = 10_000
    
    # Hard-coded sample values as per requirements (no user input, no files)
    widths = [5.0 + i * 2.3 for i in range(n)]
    heights = [3.7 - j * 0.4 if j < n // 10 else 8.9 + k * 0.6 for j, k in zip(range(0, n), list(range(j*k))) ] # Simplified generation to ensure valid floats
    
    radii = [2.5 + i * 0.3 for i in range(n)]
    
    print(f"Running benchmark with {n} shapes...")

    start_rect_time = time.perf_counter()
    total_area_rectangles = calculate_rectangle_area(widths, heights)
    end_rect_time = time.perf_counter()
    
    # For circles we can optimize slightly by pre-calculating pi if needed, 
    # but standard library math.pi is fast enough. To demonstrate algorithmic focus:
    start_circle_time = time.perf_counter()
    total_area_circles = calculate_circle_area(radii)
    end_circle_time = time.perf_counter()

    elapsed_rect = (end_rect_time - start_rect_time) * 1_000_000 # microseconds
    elapsed_circle = (end_circle_time - start_circle_time) * 1_000_000 # microseconds
    
    print(f"Rectangle Area Calculation: {total_area_rectangles:.2f} units^2")
    print(f"Circle Area Calculation:   {total_area_circles:.2f} units^2")
    
    print("--- Performance Results ---")
    print(f"Rectangles ({n}):  {elapsed_rect:.4f} microseconds (O(n))")
    print(f"Circles   ({n}):  {elapsed_circle:.4f} microseconds (O(n))")

if __name__ == '__main__':
    benchmark_comparison()