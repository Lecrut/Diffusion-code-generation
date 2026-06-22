import functools

@functools.lru_cache(maxsize=None)
def calculate_triangle_area(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height

if __name__ == "__main__":
    area1 = calculate_triangle_area(10.0, 5.0)
    area2 = calculate_triangle_area(10.0, 5.0)
    area3 = calculate_triangle_area(3.0, 4.0)
    print(area1)
    print(area2)
    print(area3)