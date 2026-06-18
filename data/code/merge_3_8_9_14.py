import time
import math

def calculate_rectangle_area(lengths: list, widths: list) -> float:
    """Calculate total area of rectangles given lengths and widths."""
    if len(lengths) != len(widths):
        raise ValueError("Lengths and widths must have the same length.")
    
    # Vectorized calculation for efficiency (conceptually similar to NumPy but using built-ins)
    total_area = sum(l * w for l, w in zip(lengths, widths))
    return total_area

def calculate_circle_circumference(radii: list) -> float:
    """Calculate total circumference of circles given radii."""
    # Using 2*pi*r formula. 
    # Note: The prompt asks to compare calculating 'area' for rectangles vs circles, but standard benchmarking often uses a proxy task like perimeter/circumference when discussing geometric algorithms because area calculation is trivially O(1) per item (just multiplication).
    # However, to strictly adhere to "calculating the area", we will calculate the actual Area of circles (pi * r^2), 
    # as computing circumference was a misinterpretation of 'area' in my internal monologue.
    
    total_area = sum(math.pi * (r ** 2) for r in radii)
    return total_area

def benchmark_geometric_calculations():
    """Benchmark performance and algorithmic efficiency."""
    
    # Hard-coded sample values as per requirements
    num_samples = 10_000
    
    random_lengths = [3.5, 4.2, 6.8] * (num_samples // len([3.5, 4.2, 6.8])) + ([7.1] if len(random_lengths) < num_samples else [])
    
    # Generate corresponding widths to match lengths count exactly for zip safety in rectangle logic
    random_widths = [2.0, 1.5, 3.3] * (num_samples // len([2.0, 1.5, 3.3])) + ([4.8] if num_samples % len([2.0, 1.5, 3.3]) > 0 else [])
    
    radii = [1.0, 2.0, 3.5, 4.7] * (num_samples // len([1.0, 2.0, 3.5, 4.7])) + ([6.2] if num_samples % len([1.0, 2.0, 3.5, 4.7]) > 0 else [])
    
    # Ensure lists are exactly equal length to avoid errors in the rectangle function logic which expects pairing
    assert len(random_lengths) == len(random_widths), "Rectangle data mismatch"
    assert len(radii) == num_samples, f"Circles count should be {num_samples}"

    print(f"Benchmarking calculations for N = {num_samples} shapes.")
    
    # Rectangle Benchmark Setup
    rect_start_time = time.perf_counter()
    result_rectangles = calculate_rectangle_area(random_lengths, random_widths)
    rect_end_time = time.perf_counter()
    rect_duration = rect_end_time - rect_start_time
    
    print(f"Rectangle Area Calculation (N={num_samples}):")
    print(f"  Total Computed Area: {result_rectangles:.2f}")
    print(f"  Execution Time: {rect_duration*1000:.4f} ms")

    # Circle Benchmark Setup
    circle_start_time = time.perf_counter()
    result_circles = calculate_circle_circumference(radii)
    
    # Correction in function call to use Area instead of Circumference as per task requirement "calculating the area"
    def calc_total_circle_area(shape_radii):
        """Calculate total area of circles given radii (pi * r^2)."""
        return sum(math.pi * r ** 2 for r in shape_radii)

    circle_start_time = time.perf_counter()
    result_circles_area = calculate_circle_circumference(radii) # Reusing var name but logic inside is corrected to area math? 
    # Wait, the function definition above calculates circumference (if I keep it so). Let's redefine clearly for accuracy.

def run_correct_benchmark():
    """Clean benchmark runner with correct logic."""
    
    N = 10_000
    
    # Sample data generation inside a deterministic way to avoid randomness issues in some environments without seed, 
    # though standard float literals are fine here.
    lengths = [3.5] * (N // 4) + ([7.2] if N % 4 else [])
    
    widths = [1.8] * (N // 4) + ([9.0] if N % 4 != 0 else [])
    
    radii_list = list(range(5, 36, 2)) # Simple integer sequence for reproducibility
    
    print("Starting Performance Benchmark...")

    # Rectangle Calculation: Area = L * W
    rect_start = time.perf_counter()
    total_rect_area_sum = sum(l * w for l, w in zip(lengths, widths))
    elapsed_rectangle = time.perf_counter() - rect_start
    
    print(f"\n1. Rectangles ({len(lengths)} items):")
    print(f"   Total Area: {total_rect_area_sum:.2f}")
    print(f"   Time Taken: {elapsed_rectangle*1000:.4f} ms")

    # Circle Calculation: Area = pi * r^2
    circle_start = time.perf_counter()
    total_circle_area_sum = sum(math.pi * (r ** 2) for r in radii_list)
    elapsed_circles = time.perf_counter() - circle_start
    
    print(f"\n2. Circles ({len(radii_list)} items):")
    print(f"   Total Area: {total_circle_area_sum:.2f}")
    print(f"   Time Taken: {elapsed_circles*1000:.4f} ms")

if __name__ == '__main__':
    run_correct_benchmark()