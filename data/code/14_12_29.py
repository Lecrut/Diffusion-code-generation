def compare_volumes(volume1, volume2):
    return volume1 == volume2

if __name__ == '__main__':
    volume1 = 100.5
    volume2 = 100.5
    result = compare_volumes(volume1, volume2)
    print(result)