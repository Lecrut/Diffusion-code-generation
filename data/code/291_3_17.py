def compare_lengths_km_m(km1, m1, km2, m2):
    if not all(isinstance(i, (int, float)) for i in [km1, m1, km2, m2]):
        raise ValueError("All inputs must be numbers")
    
    total_m1 = km1 * 1000 + m1
    total_m2 = km2 * 1000 + m2
    
    if total_m1 < total_m2:
        return -1
    elif total_m1 > total_m2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(compare_lengths_km_m(5, 300, 4, 900))
    print(compare_lengths_km_m(3, 500, 3, 500))
    print(compare_lengths_km_m(2, 750, 3, 250))