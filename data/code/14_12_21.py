def compare_volumes(volume1, volume2):
    return volume1 == volume2

if __name__ == '__main__':
    volume_a = 100.5
    volume_b = 100.5
    result = compare_volumes(volume_a, volume_b)
    print(result)