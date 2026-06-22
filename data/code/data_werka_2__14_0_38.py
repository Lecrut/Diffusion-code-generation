def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "The first volume is larger."
    elif volume1 < volume2:
        return "The second volume is larger."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume_a = 7.8
    sample_volume_b = 9.3
    comparison_result = compare_volumes(sample_volume_a, sample_volume_b)
    print(comparison_result)