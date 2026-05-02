def compare_volumes(volume_a: float, volume_b: float) -> str:
    if volume_a > volume_b:
        return "Volume A is greater"
    elif volume_b > volume_a:
        return "Volume B is greater"
    else:
        return "Volumes are equal"
if __name__ == '__main__':
    volume1 = 150.75
    volume2 = 200.50
    result = compare_volumes(volume1, volume2)
    print(result)
    volume3 = 42.0
    volume4 = 42.0
    result2 = compare_volumes(volume3, volume4)
    print(result2)
    volume5 = 300.0
    volume6 = 100.0
    result3 = compare_volumes(volume5, volume6)
    print(result3)