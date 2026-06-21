def compare_volumes(volume1, volume2):
    comparison_map = {
        1: "First volume is greater than the second.",
        -1: "First volume is less than the second.",
        0: "Both volumes are equal."
    }
    if volume1 > volume2:
        return comparison_map[1]
    elif volume1 < volume2:
        return comparison_map[-1]
    else:
        return comparison_map[0]

if __name__ == '__main__':
    volume1 = 5.6789
    volume2 = 3.14159
    result = compare_volumes(volume1, volume2)
    print(result)