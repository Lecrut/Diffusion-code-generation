def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "First volume is greater than the second."
    elif volume1 < volume2:
        return "First volume is less than the second."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    volume1 = 3.141592653589793
    volume2 = 3.141592653589793238

    result = compare_volumes(volume1, volume2)
    print(result)