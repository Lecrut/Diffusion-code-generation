def compare_volumes(volume1: float, volume2: float) -> str:
    if volume1 > volume2:
        return "volume1 is greater"
    elif volume1 < volume2:
        return "volume2 is greater"
    else:
        return "volumes are equal"

if __name__ == '__main__':
    volume_a = 50.0
    volume_b = 30.0
    result = compare_volumes(volume_a, volume_b)
    print(result)