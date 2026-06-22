def compare_volumes(volume1, volume2):
    import math
    if math.isclose(volume1, volume2, rel_tol=1e-09):
        return 'equal'
    elif volume1 > volume2:
        return 'greater than'
    else:
        return 'less than'
if __name__ == '__main__':
    volume_a = 3.141592653589793
    volume_b = 3.141592653589793
    result = compare_volumes(volume_a, volume_b)
    print(result)