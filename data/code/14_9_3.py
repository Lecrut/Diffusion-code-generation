def compare_volumes(volume1: float, volume2: float) -> str:
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2"
    elif volume1 < volume2:
        return "Volume 1 is less than Volume 2"
    else:
        return "Volume 1 is equal to Volume 2"
if __name__ == '__main__':
    v_a = 150.5
    v_b = 200.0
    result1 = compare_volumes(v_a, v_b)
    print(f"Comparing {v_a} and {v_b}: {result1}")
    v_c = 42.0
    v_d = 42.0
    result2 = compare_volumes(v_c, v_d)
    print(f"Comparing {v_c} and {v_d}: {result2}")
    v_e = 300.75
    v_f = 300.75
    result3 = compare_volumes(v_e, v_f)
    print(f"Comparing {v_e} and {v_f}: {result3}")