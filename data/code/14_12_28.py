def compare_volumes(volume1, volume2):
    return volume1 == volume2
if __name__ == '__main__':
    volume_a = 3.14159 * 5 ** 2 * 10
    volume_b = 3.14159 * 6 ** 2 * 8
    result = compare_volumes(volume_a, volume_b)
    print(result)