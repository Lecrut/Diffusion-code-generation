import time
import math

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of 10,000 rectangles given a single width and height per rectangle."""
    if len(widths) != 10_000 or len(heights) != 10_000:
        raise ValueError("Must provide exactly 10,000 dimensions for both widths and heights.")

    area = sum(w * h for w, h in zip(widths, heights))
    return area

def calculate_circle_area(radii: list[float]) -> float:
    """Calculate total area of 10,000 circles given their radii."""
    if len(radii) != 10_000:
        raise ValueError("Must provide exactly 10,000 radii.")

    # Precompute pi for slight optimization compared to importing inside loop
    total_area = sum(math.pi * r * r for r in radii)
    return total_area

if __name__ == '__main__':
    # Hard-coded sample values as required by the task constraints
    
    # Generate 10,000 random widths and heights (simulating varying rectangles)
    n = 10_000
    rectangle_widths = [float(i + 2.5 * math.random()) for i in range(n)]
    rectangle_heights = [float(3.0 + 4.0 * math.random()) for _ in range(n)]

    # Generate 10,000 random radii (simulating varying circles)
    circle_radii = [2.5 + 7.5 * math.random() for _ in range(n)]

    print("Starting rectangle area calculation...")
    start_rect_time = time.perf_counter_ns()
    
    # Run rectangle calculation twice to average out noise if needed, 
    # but here we do a single pass as per standard benchmark practice unless specified otherwise.
    rect_result = calculate_rectangle_area(rectangle_widths, rectangle_heights)

    end_rect_time = time.perf_counter_ns()
    elapsed_rect = (end_rect_time - start_rect_time) / 1_000_000_000  # Convert to seconds
    
    print(f"Rectangle total area: {rect_result:.2f} square units")
    print(f"Time taken for rectangles: {elapsed_rect:.6f} seconds")

    print("Starting circle area calculation...")
    start_circle_time = time.perf_counter_ns()
    
    # Run circle calculation
    circle_result = calculate_circle_area(circle_radii)

    end_circle_time = time.perf_counter_ns()
    elapsed_circle = (end_circle_time - start_circle_time) / 1_000_000_000  # Convert to seconds
    
    print(f"Circle total area: {circle_result:.2f} square units")
    print(f"Time taken for circles: {elapsed_circle:.6f} seconds")

    print("\n--- Performance Comparison ---")
    if elapsed_rect > 0 and elapsed_circle > 0:
        speedup = elapsed_circle / elapsed_rect
        efficiency_note = f"Circles were {speedup:.2f}x faster than rectangles." if speedup < 1 else f"Rectangles were {1/speedup:.2f}x more efficient (due to fewer multiplications per area calculation)."
    else:
        efficiency_note = "Unable to calculate relative performance due to timing errors or zero execution time."

    print(efficiency_note)