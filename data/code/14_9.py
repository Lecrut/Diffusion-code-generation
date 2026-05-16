def compare_volumes(volume_a: float, volume_b: float) -> str:
    if volume_a > volume_b:
        return "Volume A is greater than Volume B"
    elif volume_b > volume_a:
        return "Volume B is greater than Volume A"
    else:
        return "Volume A is equal to Volume B"
if __name__ == '__main__':
    volume1 = 15.5
    volume2 = 22.1
    result = compare_volumes(volume1, volume2)
    print(result)
    volume3 = 100.0
    volume4 = 100.0
    result2 = compare_volumes(volume3, volume4)
    print(result2)
    volume5 = 5.0
    volume6 = 3.5
    result3 = compare_volumes(volume5, volume6)
    print(result3)