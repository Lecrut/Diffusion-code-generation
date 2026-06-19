def compare_volumes(volume1, volume2):
    return volume1 == volume2

if __name__ == '__main__':
    volume_a = 50.0
    volume_b = 50.0
    result = compare_volumes(volume_a, volume_b)
    print(result)