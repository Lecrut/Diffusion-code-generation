def compare_volumes(volume1: str, volume2: str) -> bool:
    num1 = float(volume1.split()[0])
    num2 = float(volume2.split()[0])
    return num1 > num2
if __name__ == '__main__':
    sample_volume1 = '3.56 m^3'
    sample_volume2 = '2.89 m^3'
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)