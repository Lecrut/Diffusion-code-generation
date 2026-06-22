def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "First volume is greater than the second."
    elif volume1 < volume2:
        return "First volume is less than the second."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 6.54321
    sample_volume2 = 6.54321
    comparison_result = compare_volumes(sample_volume1, sample_volume2)
    print(comparison_result)