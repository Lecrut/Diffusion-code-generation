def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "First volume is greater than the second."
    if volume1 < volume2:
        return "First volume is less than the second."
    return "Both volumes are equal."

if __name__ == '__main__':
    volume1 = 6.0
    volume2 = 3.14
    result = compare_volumes(volume1, volume2)
    print(result)