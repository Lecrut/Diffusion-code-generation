def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "Volume 1 is larger"
    elif volume1 < volume2:
        return "Volume 2 is larger"
    else:
        return "Both volumes are equal"

if __name__ == '__main__':
    volume1 = 350.75
    volume2 = 499.20
    result = compare_volumes(volume1, volume2)
    print(result)