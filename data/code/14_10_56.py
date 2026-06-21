def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
    elif volume1 < volume2:
        return f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1})."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume_a = 700
    sample_volume_b = 700
    comparison_result = compare_volumes(sample_volume_a, sample_volume_b)
    print(comparison_result)