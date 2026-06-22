def compare_volumes(volume1, volume2):
    if not (isinstance(volume1, (int, float)) and isinstance(volume2, (int, float))):
        raise ValueError("Both volumes must be numbers")

    result = {
        "volume1": volume1,
        "volume2": volume2,
        "ratio": None,
        "are_equal": False
    }

    if volume1 == volume2:
        result["are_equal"] = True
    else:
        larger_volume = max(volume1, volume2)
        smaller_volume = min(volume1, volume2)
        result["ratio"] = larger_volume / smaller_volume

    return result

if __name__ == '__main__':
    sample_volumes = [(10, 5), (7, 7), (3.5, 14)]
    for v1, v2 in sample_volumes:
        print(compare_volumes(v1, v2))