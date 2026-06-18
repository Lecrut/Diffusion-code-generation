import time
from math import pi as PI

def calculate_rectangle_area(width: float, height: float) -> None:
    """Calculate area of a single rectangle."""
    return width * height

def calculate_circle_area(radius: float) -> None:
    """Calculate area of a single circle using PI constant for precision."""
    return radius ** 2 * PI

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file I/O is required.
    num_rectangles = 10_000
    num_circles = 10_000
    
    rect_widths = [5.0] * num_rectangles
    rect_heights = [3.0] * num_rectangles
    
    circle_radii = [2.0, 4.0, 6.0, 8.0] 
    # Using a list of varying radii to simulate real-world variability instead of constant values for meaningful comparison

    start_time_total = time.perf_counter()
    
    # Benchmark rectangles
    total_rect_area_sum = 0.0
    for i in range(num_rectangles):
        area_result = calculate_rectangle_area(rect_widths[i], rect_heights[i])
        total_rect_area_sum += area_result
    
    end_time_total = time.perf_counter()

    print(f"Rectangle Benchmark Results:")
    print(f"  Calculated Area of {num_rectangles} Rectangles")
    
    # Calculate average execution time per rectangle for rectangles
    avg_time_per_rectangle = (end_time_total - start_time_total) / num_rectangles
    
    print(f"\n--- Rectangle Performance ---\n")

    rect_area_result_sum = 0.0
    circle_area_result_sum = 0.0
    
    # Benchmark circles using the same time window for comparison purposes, but separate calculation loops to isolate performance differences accurately without mixing operations in a single loop which could introduce overhead bias.
    
    start_time_circles = time.perf_counter()
    for i in range(num_circles):
        area_result = calculate_circle_area(circle_radii[i])
        circle_area_result_sum += area_result
    
    end_time_circles = time.perf_counter()

    print(f"Circle Benchmark Results:")
    print(f"  Calculated Area of {num_circles} Circles")
    
    avg_time_per_circle = (end_time_circles - start_time_circles) / num_circles
    
    # Comparison Analysis Section
    total_runtime_seconds = end_time_total + (end_time_circles - start_time_circles)
    
    print(f"\n--- Comparative Algorithmic Efficiency ---\n")

    rect_avg_area_sum = total_rect_area_sum / num_rectangles if num_rectangles > 0 else 0.0
    
    circle_avg_area_sum = circle_area_result_sum / num_circles if num_circles > 0 else 0.0

    print(f"Average Area per Rectangle: {rect_avg_area_sum:.4f}")
    print(f"Average Area per Circle:   {circle_avg_area_sum:.6f} (using precise PI)")
    
    rect_performance_metrics = f"{avg_time_per_rectangle:.8f}"
    circle_performance_metrics = f"{avg_time_per_circle:.8f}"

    performance_ratio = float(circle_performance_metrics) / float(rect_performance_metrics) if rect_performance_metrics != '0.0' else 1.0
    
    print(f"Average Time per Operation (Rectangles): {rect_performance_metrics}")
    
    # Ensure we do not divide by zero or create invalid metrics for the circles performance report as well to maintain consistency in output format and structure across both benchmarks.

    if circle_performance_metrics != '0.0':
        print(f"Average Time per Operation (Circles):   {circle_performance_metrics}")

    print("\nAlgorithmic Efficiency Analysis:")
    
    # Provide a textual analysis of the algorithmic complexity rather than just raw numbers to explain why circles might be slightly slower due to floating point multiplication vs simple addition logic.
    rect_ops = f"Rectangles use O(1) operations (multiplication)."
    circle_ops = "Circles involve additional constant lookup and potentially more complex arithmetic."

    print(f"\n  Rectangular Area Calculation Complexity: {rect_ops}")
    
    # Output the final comparison result in a clear, readable format.
    if performance_ratio > 1.0:
        slowdown_factor = f"{performance_ratio * 2:.4f}x" 
        slower_algorithm_name = "Circles (due to PI constant and floating point operations)"
        
        print(f"\n  Performance Ratio Comparison ({rect_performance_metrics}: {slowdown_factor})")
    else:
        faster_algorithm_name = "Rectangles (simpler multiplicative logic with fewer constants involved per operation)"
        print(f"Performance Ratio Comparison ({circle_performance_metrics} vs {rect_performance_metrics}): {faster_algorithm_name}")