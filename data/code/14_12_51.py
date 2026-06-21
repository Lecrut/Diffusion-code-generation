def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "First volume is greater than the second."
    if volume1 < volume2:
        return "First volume is less than the second."
    return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 6.7890
    sample_volume2 = 3.14159
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)