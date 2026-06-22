def compare_volumes(volume1, volume2):
    import math
    if math.isclose(volume1, volume2):
        return 'equal'
    elif volume1 > volume2:
        return 'greater than'
    else:
        return 'less than'
if __name__ == '__main__':
    volume1 = 3.141592653589793
    volume2 = 3.141592653589793
    result = compare_volumes(volume1, volume2)
    print(result)