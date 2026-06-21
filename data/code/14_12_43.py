def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    if volume1 > volume2:
        return 1
    elif volume1 < volume2:
        return -1
    else:
        return 0

COMPARISON_MESSAGES = {
    1: "First volume is greater than the second.",
    -1: "First volume is less than the second.",
    0: "Both volumes are equal."
}

if __name__ == '__main__':
    try:
        volume1 = 2.71828
        volume2 = 3.14159
        comparison_result = compare_volumes(volume1, volume2)
        print(COMPARISON_MESSAGES[comparison_result])
    except ValueError as e:
        print(e)