import math

def are_volumes_equal(volume1, volume2, rel_tol=1e-9):
    return math.isclose(volume1, volume2, rel_tol=rel_tol)

if __name__ == '__main__':
    sample_volume1 = 100.0
    sample_volume2 = 100.000000001
    result = are_volumes_equal(sample_volume1, sample_volume2)
    print(result)