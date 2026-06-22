def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "The first volume is larger."
    if volume1 < volume2:
        return "The second volume is larger."
    return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 7.8
    sample_volume2 = 7.8
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)