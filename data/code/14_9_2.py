def compare_volumes(volume1: float, volume2: float) -> float:
    return abs(volume1 - volume2)
if __name__ == '__main__':
    v1 = 15.5
    v2 = 22.3
    result = compare_volumes(v1, v2)
    print(result)