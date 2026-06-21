def compare_volumes(volume1, volume2):
    greater_than = " is greater than "
    if volume1 > volume2:
        return f"Volume 1 ({volume1}){greater_than}Volume 2 ({volume2})."
    elif volume1 < volume2:
        return f"Volume 2 ({volume2}){greater_than}Volume 1 ({volume1})."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume_a = 800
    sample_volume_b = 600
    comparison_result = compare_volumes(sample_volume_a, sample_volume_b)
    print(comparison_result)