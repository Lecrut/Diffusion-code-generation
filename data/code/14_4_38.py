import math
RELATIVE_TOLERANCE = 1e-09
ABSOLUTE_TOLERANCE = 0.0

def are_volumes_equal(volume1, volume2):
    return math.isclose(volume1, volume2, rel_tol=RELATIVE_TOLERANCE, abs_tol=ABSOLUTE_TOLERANCE)
if __name__ == '__main__':
    volume_a = 50.0
    volume_b = 50.0000000001
    result = are_volumes_equal(volume_a, volume_b)
    print(result)