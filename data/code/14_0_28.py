def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "First volume is larger."
    elif volume1 < volume2:
        return "Second volume is larger."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 5.75
    sample_volume2 = 3.20
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)