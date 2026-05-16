def compare_volumes(volume1: float, volume2: float) -> str:
    if volume1 > volume2:
        return "Volume 1 is greater"
    elif volume2 > volume1:
        return "Volume 2 is greater"
    else:
        return "Volumes are equal"
if __name__ == '__main__':
    v_a = 150.75
    v_b = 200.50
    result1 = compare_volumes(v_a, v_b)
    print(f"Comparing {v_a} and {v_b}: {result1}")
    v_c = 33.33
    v_d = 33.33
    result2 = compare_volumes(v_c, v_d)
    print(f"Comparing {v_c} and {v_d}: {result2}")
    v_e = 500.0
    v_f = 499.99
    result3 = compare_volumes(v_e, v_f)
    print(f"Comparing {v_e} and {v_f}: {result3}")