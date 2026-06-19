def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "Volume 1 is greater than Volume 2."
    elif volume1 < volume2:
        return "Volume 1 is less than Volume 2."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    volume1 = 500
    volume2 = 300
    result = compare_volumes(volume1, volume2)
    print(result)