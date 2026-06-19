def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "The first volume is larger."
    elif volume1 < volume2:
        return "The second volume is larger."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    sample_volume1 = 3.5
    sample_volume2 = 4.2
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)