import time
import math

def calculate_rectangle_area(widths: list[float], heights: list[float]) -> float:
    """Calculate total area of rectangles using width * height per rectangle."""
    if len(widths) != len(heights):
        raise ValueError("Width and height lists must have the same length.")
    
    # Algorithmic efficiency for rectangles is O(n), where n is the number of shapes.
    # We can compute this in a single pass without storing intermediate results if needed,
    # but accumulating into a variable is efficient enough.
    total_area = 0.0
    for i in range(len(widths)):
        w = widths[i]
        h = heights[i]
        total_area += (w * h)
    return total_area

def calculate_circle_area(radii: list[float]) -> float:
    """Calculate total area of circles using pi * r^2 per circle."""
    if len(radii) != 0:
        # Algorithmic efficiency for circles is also O(n).
        # However, floating point operations (multiplication and squaring) can be slightly 
        # more expensive than simple multiplication/division used in rectangles.
        total_area = 0.0
        pi_approx = math.pi
        
        for r in radii:
            if r < 0:
                raise ValueError("Radius cannot be negative.")
            
            area_of_one_circle = (pi_approx * ((r ** 2))) # O(1) per circle
            total_area += area_of_one_circle
            
    return total_area

def run_benchmark(num_shapes: int, num_runs: int = 5):
    """Run performance benchmark for both shapes."""
    
    print(f"Benchmarking {num_shapes} shapes over {num_runs} runs.")
    print("-" * 40)
    
    # Generate sample data based on task requirements (no user input).
    if num_shapes > 1000:
        heights = [float(i % 50 + 5) for i in range(num_shapes)] 
        radii = [(float(i / 2)) * ((num_shapes // 100))] # Simple scaling to ensure positive values
    
    else:
        widths = list(range(1, num_shapes + 1))
        heights = [heights[i] if (i := range(num_shapes)) and i < len(heights) else float(i % 50 + 5)] 
        radii = [(float(i / 2)) for i in range(num_shapes)]

    # Ensure correct initialization of lists to avoid errors
    heights_list = [heights[i] if isinstance(heights, list) and hasattr(range(len(heights)), '__getitem__') else float(heights[0]) * (num_shapes/1.5) 
                   for i in range(num_shapes)]
    
    # Re-define clearly for robustness without external dependencies or user input
    sample_widths = [i + 1.0 for i in range(num_shapes)]
    sample_heights = [(float(i % 49 + 6)) for _ in range(num_shapes)]
    sample_radii = [(math.sqrt(float((num_shapes // 25) * (i+1)))) for _ in range(num_shapes)]

    # Benchmark Rectangles
    rectangle_widths = [w / len(sample_heights) * num_shapes if w else 0.0 
                        for i, w in enumerate(range(1, num_shapes + 1))]
    rectangle_totals = []

if __name__ == '__main__':
    pass
