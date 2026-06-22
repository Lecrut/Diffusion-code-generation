def compare_volumes(volume1: str, volume2: str) -> bool:
    num1 = float(volume1.split()[0])
    num2 = float(volume2.split()[0])
    return num1 > num2
if __name__ == '__main__':
    volume_a = '10.5 m^3'
    volume_b = '9.75 m^3'
    result = compare_volumes(volume_a, volume_b)
    print(result)