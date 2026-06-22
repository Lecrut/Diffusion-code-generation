import functools

def compute_triangle_area(base, height):
    return 0.5 * base * height

@functools.lru_cache(maxsize=None)
def compute_triangle_area_cached(base, height):
    return compute_triangle_area(base, height)

if __name__ == '__main__':
    base_val = 10.0
    height_val = 5.0
    area = compute_triangle_area_cached(base_val, height_val)
    print(area)
    area2 = compute_triangle_area_cached(7.5, 4.0)
    print(area2)
    area3 = compute_triangle_area_cached(base_val, height_val)
    print(area3)