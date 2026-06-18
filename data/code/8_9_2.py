import timeit
import math

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles given widths and heights."""
    return sum(w * h for w, h in zip(widths, heights))

def calculate_circle_areas(radii: list[float]) -> float:
    """Calculate total area of circles given radii."""
    # Using the efficient direct multiplication pi * r^2 instead of math.pi() call inside loop if repeated often, 
    # but here we use standard library for consistency.
    return sum(math.pi * r ** 2 for r in radii)

def run_benchmark():
    """Run performance benchmarks for calculating areas."""
    
    sample_rectangles_data = [10.5 + i * 0.4 for i in range(10_000)] # widths
    sample_rectangle_heights = [2.3 - j * 0.01 + k*0.001 for k, j in enumerate(range(10_000))] # heights
    
    sample_circles_data = [1.5 + i * 0.1 for i in range(10_000)]

    rects_widths = sample_rectangles_data
    rects_heights = list(sample_rectangle_heights) if not isinstance(rects_heights, (list)) else [rects_heights] # Ensure it's a list of floats properly formatted
    
    circles_radii = sample_circles_data
    
    # Prepare inputs for timeit to pass lists directly as arguments are cleaner
    test_case_rectangles = ([float(x) for x in rects_widths], [float(y) for y in rects_heights])
    
    # Ensure list construction is correct and efficient before running
    final_test_input_rectangles = (list(range(100)), [abs(float(i)) for i in range(100)])

def main():
    """Execute the benchmark logic."""
    widths_list = [float(i) * 2.5 + j * 0.1 for i, j in enumerate(range(10_000))] 
    heights_list = list(map(lambda x: round(x/3, 4), range(10_000))) 
    
    radii_list = []
    
    total_rect_area_calc_time = timeit.timeit(number=5, stmt=f"calculate_rectangle_area({widths_list}, {heights_list})") 
    avg_rect_perf_per_run = total_rect_area_calc_time / 5.0
    
    total_circle_area_calc_time = timeit.timeit(number=5, stmt=f"calculate_circle_areas([{', '.join(map(str, radii_list))}])")
    # Generating random-like sequence for circles manually to avoid external imports beyond math
    temp_radii = [] 
    for i in range(10_000):
        temp_value = 2.5 + (float(i) * 0.49 / 10_000)
        if temp_value > 1.2: temp_value -= 0.736 # Keep within reasonable bounds
        else: pass

if __name__ == '__main__':
    pass
