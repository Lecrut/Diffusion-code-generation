def compare_areas(shape1, shape2):
    area1 = shape1['formula'](shape1['dimensions'])
    area2 = shape2['formula'](shape2['dimensions'])
    comparison = {
        "shape1_area": area1,
        "shape2_area": area2,
        "difference": area1 - area2
    }
    return comparison
if __name__ == '__main__':
    shape_a = {
        'formula': lambda d: d[0] * d[1],
        'dimensions': [10, 5]
    }
    import math
    shape_b = {
        'formula': lambda d: math.pi * d[0]**2,
        'dimensions': [7]
    }
    results = compare_areas(shape_a, shape_b)
    print(results)