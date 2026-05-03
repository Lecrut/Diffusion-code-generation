import math
def are_volumes_close(volume1, volume2, tolerance=1e-9):
    return math.isclose(volume1, volume2, abs_tol=tolerance)
if __name__ == '__main__':
    v1 = 10.0
    v2 = 10.000000000000001
    v3 = 10.000000001
    v4 = 10.0000001
    v5 = 10.000001
    print(f"Comparing {v1} and {v2}: {are_volumes_close(v1, v2)}")
    print(f"Comparing {v1} and {v3}: {are_volumes_close(v1, v3)}")
    print(f"Comparing {v1} and {v4}: {are_volumes_close(v1, v4)}")
    print(f"Comparing {v1} and {v5}: {are_volumes_close(v1, v5)}")
    print(f"Comparing 5.0 and 5.0: {are_volumes_close(5.0, 5.0)}")
    print(f"Comparing 5.0 and 5.000000000000001: {are_volumes_close(5.0, 5.000000000000001)}")
    print(f"Comparing 1.0 and 2.0: {are_volumes_close(1.0, 2.0)}")