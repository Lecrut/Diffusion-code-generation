import math

def are_volumes_equal(volume1, volume2, rel_tol=1e-9, abs_tol=0.0):
    return math.isclose(volume1, volume2, rel_tol=rel_tol, abs_tol=abs_tol)

if __name__ == '__main__':
    sample_volume_a = 57.2958
    sample_volume_b = 57.295800001
    comparison_result = are_volumes_equal(sample_volume_a, sample_volume_b)
    print(comparison_result)