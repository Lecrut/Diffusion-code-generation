def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "First volume is greater than the second."
    elif volume1 < volume2:
        return "First volume is less than the second."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    volume_a = 3.141592653589793
    volume_b = 3.1415926535897932
    result = compare_volumes(volume_a, volume_b)
    print(result)