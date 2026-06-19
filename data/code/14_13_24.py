import math

def compare_volumes(volume1, volume2):
    epsilon = 1e-09
    if math.isclose(volume1, volume2, abs_tol=epsilon):
        return 'equal'
    elif volume1 > volume2:
        return 'greater than'
    else:
        return 'less than'
if __name__ == '__main__':
    volume_a = 3.141592653589793
    volume_b = 3.141592653589792
    result = compare_volumes(volume_a, volume_b)
    print(result)