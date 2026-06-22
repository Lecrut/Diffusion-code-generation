def get_larger_in_original_unit(meters1, meters2):
    if meters1 is None or meters2 is None:
        raise ValueError("Both arguments must be numbers")
    centimeters1 = meters1 * 100
    centimeters2 = meters2 * 100
    if centimeters1 > centimeters2:
        return meters1
    return meters2

if __name__ == '__main__':
    val1 = 1.5
    val2 = 2.3
    result = get_larger_in_original_unit(val1, val2)
    print(result)