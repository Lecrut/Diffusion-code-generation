def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return f"Volume 1 ({volume1}) is larger than Volume 2 ({volume2})."
    elif volume1 < volume2:
        return f"Volume 2 ({volume2}) is larger than Volume 1 ({volume1})."
    else:
        return "Both volumes are of equal size."

if __name__ == '__main__':
    first_volume = 1000
    second_volume = 250
    comparison_outcome = compare_volumes(first_volume, second_volume)
    print(comparison_outcome)