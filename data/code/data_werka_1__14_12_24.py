def compare_volumes(volume1, volume2):
    return volume1 == volume2
if __name__ == '__main__':
    volume_a = 3.14159 * 2 * 2 * 2
    volume_b = 3.14159 * 3 * 3 * 3
    result = compare_volumes(volume_a, volume_b)
    print(result)