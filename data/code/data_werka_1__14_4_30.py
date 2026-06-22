import math

def are_volumes_equal(volume1, volume2, rel_tol=1e-9):
    return math.isclose(volume1, volume2, rel_tol=rel_tol)

if __name__ == '__main__':
    sample_volume1 = 0.0000001234
    sample_volume2 = 0.0000001235
    result = are_volumes_equal(sample_volume1, sample_volume2)
    print(result)