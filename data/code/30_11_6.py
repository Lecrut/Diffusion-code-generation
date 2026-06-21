import math

def get_radius_by_name(name):
    lookup = {
        "default": 5,
        "small": 1,
        "large": 10
    }
    return lookup.get(name, 0)

def compute_area(r):
    return math.pi * r * r

if __name__ == '__main__':
    target_key = "default"
    radius_val = get_radius_by_name(target_key)
    area_result = compute_area(radius_val)
    print(area_result)