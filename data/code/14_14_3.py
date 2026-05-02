def volume_analyzer(volume1, volume2):
    if volume1 < volume2:
        larger = volume2
        smaller = volume1
    else:
        larger = volume1
        smaller = volume2
    ratio = larger / smaller
    are_equal = larger == smaller
    return {
        "volume1": volume1,
        "volume2": volume2,
        "ratio_larger_to_smaller": ratio,
        "are_equal": are_equal
    }
if __name__ == '__main__':
    v1 = 10
    v2 = 15
    result = volume_analyzer(v1, v2)
    print(result)
    v3 = 7
    v4 = 7
    result2 = volume_analyzer(v3, v4)
    print(result2)
    v5 = 20
    v6 = 5
    result3 = volume_analyzer(v5, v6)
    print(result3)