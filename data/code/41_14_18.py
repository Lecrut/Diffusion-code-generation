def compute_area(d1, d2):
    if d1 < 0 or d2 < 0:
        return 0.0
    product = d1 * d2
    half = product * 0.5
    return half

if __name__ == '__main__':
    d1_val = 12.0
    d2_val = 7.0
    area_result = compute_area(d1_val, d2_val)
    print(area_result)