VOLUME_COMPARISON_THRESHOLD = 1e-9

def compare_volumes(volume1, volume2):
    if abs(volume1 - volume2) < VOLUME_COMPARISON_THRESHOLD:
        return "Both volumes are equal."
    elif volume1 > volume2:
        return "The first volume is larger."
    else:
        return "The second volume is larger."

if __name__ == '__main__':
    sample_volume1 = 7.8
    sample_volume2 = 7.800000001
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)