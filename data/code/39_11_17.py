def compute_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return base_area * height

if __name__ == '__main__':
    result1 = compute_prism_volume(10, 5)
    print(result1)
    
    result2 = compute_prism_volume(7.5, 4)
    print(result2)
    
    result3 = compute_prism_volume(0, 10)
    print(result3)