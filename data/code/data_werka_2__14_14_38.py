def compare_volumes(volume1: str, volume2: str) -> bool:
    num1 = float(volume1.split()[0])
    num2 = float(volume2.split()[0])
    return num1 > num2
if __name__ == '__main__':
    vol1 = '3.56 m^3'
    vol2 = '2.89 m^3'
    result = compare_volumes(vol1, vol2)
    print(result)