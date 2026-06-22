def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if any(side < 0 for side in (side_a, side_b, side_c)):
        raise ValueError("Side lengths cannot be negative.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides = {
        'side_a': 7.5,
        'side_b': 9.2,
        'side_c': 10.3
    }
    
    try:
        perimeter = calculate_triangle_perimeter(sample_sides['side_a'], sample_sides['side_b'], sample_sides['side_c'])
        print(f"Side A: {sample_sides['side_a']}")
        print(f"Side B: {sample_sides['side_b']}")
        print(f"Side C: {sample_sides['side_c']}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")