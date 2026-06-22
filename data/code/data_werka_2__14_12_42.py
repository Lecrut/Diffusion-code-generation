def compare_volumes(volume1, volume2):
    comparison_map = {
        1: "First volume is greater than the second.",
        -1: "First volume is less than the second.",
        0: "Both volumes are equal."
    }
    result_key = (volume1 > volume2) - (volume1 < volume2)
    return comparison_map[result_key]

if __name__ == '__main__':
    volume1 = 6.7890
    volume2 = 3.14159
    result = compare_volumes(volume1, volume2)
    print(result)