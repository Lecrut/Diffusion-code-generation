def compute_prism_volume(base_area, height):
    if base_area <= 0 or height <= 0:
        return 0.0
    return base_area * height

if __name__ == '__main__':
    result1 = compute_prism_volume(10, 5)
    print(result1)
    
    result2 = compute_prism_volume(3.5, 2.0)
    print(result2)
    
    result3 = compute_prism_volume(0, 5)
    print(result3)