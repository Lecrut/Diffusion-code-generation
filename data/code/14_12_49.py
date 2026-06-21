TOLERANCE = 1e-9

def compare_volumes(volume1, volume2):
    if abs(volume1 - volume2) < TOLERANCE:
        return "Both volumes are equal."
    elif volume1 > volume2:
        return "First volume is greater than the second."
    else:
        return "First volume is less than the second."

if __name__ == '__main__':
    volume1 = 6.28318
    volume2 = 3.14159
    result = compare_volumes(volume1, volume2)
    print(result)