def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "Volume 1 is larger."
    elif volume1 < volume2:
        return "Volume 2 is larger."
    else:
        return "Volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 5.2
    sample_volume2 = 3.8
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)