import math

def are_volumes_equal(volume1, volume2, rel_tol=1e-9):
    return math.isclose(volume1, volume2, rel_tol=rel_tol)

if __name__ == '__main__':
    volume_a = 3.141592653589793
    volume_b = 3.141592653589794
    result = are_volumes_equal(volume_a, volume_b)
    print(result)