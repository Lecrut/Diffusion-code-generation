def compare_volumes(volume1, volume2):
    comparison_map = {
        1: f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2}).",
        -1: f"Volume 2 ({volume2}) is greater than Volume 1 ({volume1}).",
        0: "Both volumes are equal."
    }
    return comparison_map[(volume1 > volume2) - (volume1 < volume2)]

if __name__ == '__main__':
    sample_volume_a = 650
    sample_volume_b = 650
    result = compare_volumes(sample_volume_a, sample_volume_b)
    print(result)