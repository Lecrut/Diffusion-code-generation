def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "Volume 1 is larger."
    elif volume1 < volume2:
        return "Volume 2 is larger."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 3.14
    sample_volume2 = 2.71
    print(compare_volumes(sample_volume1, sample_volume2))