import math

def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

def compute_multiple_areas(bases, heights):
    results = []
    for b, h in zip(bases, heights):
        results.append(calculate_triangle_area(b, h))
    return results

if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.0
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)
    
    multi_bases = [3.0, 7.0, 12.0]
    multi_heights = [4.0, 2.0, 8.0]
    multi_results = compute_multiple_areas(multi_bases, multi_heights)
    for val in multi_results:
        print(val)