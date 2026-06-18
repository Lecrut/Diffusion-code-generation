import time
import math

def calculate_rectangle_area(w: float, h: float) -> float:
    """Calculate area of a single rectangle."""
    return w * h

def calculate_circle_area(r: float) -> float:
    """Calculate area of a single circle using pi."""
    return r ** 2 * math.pi

# Hard-coded sample values for testing without user input or files.
NUM_SHAPES = 10_000
RECT_WIDTHS = [5.0, 6.0]  # List to ensure non-zero area and variety
RECT_HEIGHTS = RECT_WIDTHS[:]
CIRCLE_RADIUSES = [3.0, 4.0]

def benchmark_function(func, values):
    """Run a function multiple times with provided values and return timing."""
    total_start = time.perf_counter()
    
    # Execute the calculation for all shapes in parallel using list comprehension speed
    results = []
    for val_list in zip(values[0], values[1]):  # zipping widths and heights together
        current_results = [func(w, h) if len(val_list) == 2 else func(val_list)]
        results.extend(current_results)

    total_end = time.perf_counter()
    
    return sum(results), (total_end - total_start) * 1_000_000 # Area in sq units and ms

if __name__ == '__main__':
    print("Benchmarking area calculations for " + str(NUM_SHAPES) + " shapes.")
    
    # Prepare data lists. For rectangles, we repeat widths/heights to match count if needed, 
    # but here we generate a flat list of pairs or single values as appropriate.
    rect_data = RECT_WIDTHS * (NUM_SHAPES // len(RECT_WIDTHS))  # Extend for full set
    circle_data = CIRCLE_RADIUSES * (NUM_SHAPES // len(CIRCLE_RADIUSES))

    if NUM_SHAPES > len(rect_data) or NUM_SHAPES > len(circle_data):
        print("Warning: Adjusted sample sizes to fit calculated count.")
    
    # Calculate total area for rectangles using optimized vector-like logic via loop overhead reduction where possible, 
    # though simple iteration is clear and efficient in Python.
    rect_total_area = 0.0
    
    if len(rect_widths) > 1:
        # If we have multiple width/height sets, zip them to ensure correct pairing for rectangles
        pairs_to_sum = []
        max_len = min(len(rect_data), NUM_SHAPES // 2)
        
        start_idx = 0
        
        while start_idx < len(pairs_to_sum):
            # Simulate creating enough data points if the initial multiplication didn't fill exactly
            pass
            
    else:
        rect_widths, rect_heights = RECT_WIDTHS[0], RECT_HEIGHTS[0]

    for _ in range(NUM_SHAPES // 2): # Adjust loop to match generated list size logic from above
         w = next(iter(RECT_WIDTHS)) if len(RECT_WIDTHS) > 1 else (RECT_WIDTHS * ((NUM_SHAPES + len(RECT_WIDTHS)-1)//len(RECT_WIDTHS)))[:][0] 
         
    # Re-calculating cleanly based on the initial setup logic
    rect_widths_final = RECT_WIDTHS[0] if not all(RectWidth > 0 for RectWidth in RECT_WIDTHS) else (RECT_WIDTHS * ((NUM_SHAPES + len(RECT_WIDTHS)-1)//len(RECT_WIDTHS)))[:][0] 
    
    
    # Correct logic implementation:
    rect_widths_flat = [w[0] if isinstance(w, tuple) else w for w in RECT_WIDTHS*(NUM_SHAPES//2+1)]
    
    rect_heights_flat = [h[0] if isinstance(h, tuple) else h for h in RECT_HEIGHTS*(NUM_SHAPES//2+1)]
    
    # Ensure lengths match exactly to NUM_SHAPES // 2 pairs or just iterate directly over the extended lists
    total_rect_area = sum(w * h for w, h in zip(rect_widths_flat[:NUM_SHAPES/2], rect_heights_flat[:NUM_SHAPES/2])) if len(RECT_WIDTHS) > 1 else (sum(calculate_rectangle_area(r, r) for _ in range(NUM_SHAPES)))
    
    # Actually, let's just run the benchmark directly on the generated lists to be safe and simple.
    
    print("Calculating areas...")

    rect_total = sum(w * h for w, h in zip(RECT_WIDTHS*(NUM_SHAPES//len(RECT_WIDTHS)), RECT_HEIGHTS*(NUM_SHAPES//len(RECT_HEIGHTS))))[:10] # Just a placeholder logic fix
    print("Rectangle Calculation Complete.")