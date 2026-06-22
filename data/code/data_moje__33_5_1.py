import functools

@functools.lru_cache(maxsize=None)
def compute_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height

if __name__ == '__main__':
    area1 = compute_triangle_area(10, 5)
    area2 = compute_triangle_area(7, 3)
    area3 = compute_triangle_area(10, 5)
    print(area1)
    print(area2)
    print(area3)