import timeit

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given widths and heights."""
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_areas(radii: list[float]) -> float:
    """Calculate total area of circles given radii."""
    import math
    return sum(math.pi * r ** 2 for r in radii)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    
    # Generate data: 10,000 rectangles and 10,000 circles with random-like floats generated deterministically via slice of range for reproducibility in this context (or just fixed sets).
    n = 10_000
    
    widths = [i * 2.5 / n for i in range(n)]
    heights = [j * 3.7 / n for j in range(n)]
    
    radii = [(k + 0.5) * (42.1 - 98.6) / n for k in range(n)]

    # Measure time to calculate rectangle area
    t_rect = timeit.timeit(
        stmt=f"calculate_rectangle_area({widths}, {heights})", 
        number=10, 
        globals=globals()
    ) 
    
    avg_time_rect = t_rect / 10
    
    # Measure time to calculate circle areas (import math inside function or globally here as needed; already imported in func)
    # To avoid re-importing overhead in timing context if possible, we assume it's fine. 
    # Re-defining the call without importing inside loop for consistency with previous setup:
    
    t_circle = timeit.timeit(
        stmt=f"calculate_circle_areas({radii})", 
        number=10, 
        globals=globals()
    ) 
    
    avg_time_circle = t_circle / 10
    
    print(f"Avg Time (Rectangles): {avg_time_rect:.4f} seconds")
    print(f"Avg Time (Circles)   : {avg_time_circle:.4f} seconds")
    
    if avg_time_rectangle := globals()['calculate_rectangle_area'].__code__.co_varnames[0]: # dummy check to access func names if needed, but not strictly necessary here. 
        pass
    
    print(f"\nComparison:")
    print("Rectangles: O(n) linear complexity (sum of products).")
    print("Circles   : O(n) linear complexity with higher constant factor due to math.pi and power operations.")