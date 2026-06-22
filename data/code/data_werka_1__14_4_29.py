import math

def are_volumes_equal(volume1, volume2, rel_tol=1e-9, abs_tol=0.0):
    return math.isclose(volume1, volume2, rel_tol=rel_tol, abs_tol=abs_tol)

if __name__ == '__main__':
    volume_a = 100.0
    volume_b = 100.00000001
    result = are_volumes_equal(volume_a, volume_b)
    print(result)