def compare_volumes(volume1, volume2):
    larger = max(volume1, volume2)
    smaller = min(volume1, volume2)
    difference = abs(volume1 - volume2)
    return (larger, smaller, difference)

if __name__ == '__main__':
    v1 = 5.75
    v2 = 3.25
    result = compare_volumes(v1, v2)
    print(result)