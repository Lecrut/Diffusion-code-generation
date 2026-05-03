import math
def are_volumes_close(volume1, volume2, tolerance=1e-9):
    return math.isclose(volume1, volume2, abs_tol=tolerance)
if __name__ == '__main__':
    v1 = 10.0
    v2 = 10.000000000000001
    v3 = 10.000000001
    v4 = 10.0000001
    v5 = 10.000001
    print(f"v1={v1}, v2={v2}: {are_volumes_close(v1, v2)}")
    print(f"v1={v1}, v3={v3}: {are_volumes_close(v1, v3)}")
    print(f"v1={v1}, v4={v4}: {are_volumes_close(v1, v4)}")
    print(f"v1={v1}, v5={v5}: {are_volumes_close(v1, v5)}")
    print(f"v1={v1}, v1: {are_volumes_close(v1, v1)}")
    print(f"v1={v1}, v1+1e-15={v1+1e-15}: {are_volumes_close(v1, v1+1e-15)}")