import math
def compare_volumes(volume1, volume2):
    if volume1 == volume2:
        difference = 0.0
        comparison = "The volumes are exactly the same."
    elif volume1 > volume2:
        difference = volume1 - volume2
        comparison = f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
    else:
        difference = volume2 - volume1
        comparison = f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1})."
    return comparison, difference
if __name__ == '__main__':
    v_a = 15.75
    v_b = 15.75
    result_a, diff_a = compare_volumes(v_a, v_b)
    print(f"Comparison 1: {result_a}")
    print(f"Difference 1: {diff_a}")
    print("-" * 20)
    v_c = 10.0
    v_d = 22.5
    result_b, diff_b = compare_volumes(v_c, v_d)
    print(f"Comparison 2: {result_b}")
    print(f"Difference 2: {diff_b}")
    print("-" * 20)
    v_e = 50.1
    v_f = 49.8
    result_c, diff_c = compare_volumes(v_e, v_f)
    print(f"Comparison 3: {result_c}")
    print(f"Difference 3: {diff_c}")