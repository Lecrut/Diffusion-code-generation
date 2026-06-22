def compare_volumes(volume1, volume2):
    comparison_map = {
        1: "First volume is greater than the second.",
        -1: "First volume is less than the second.",
        0: "Both volumes are equal."
    }
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    result_code = 0
    if volume1 > volume2:
        result_code = 1
    elif volume1 < volume2:
        result_code = -1
    
    return comparison_map[result_code]

if __name__ == '__main__':
    try:
        volume1 = 6.7890
        volume2 = 3.14159
        result = compare_volumes(volume1, volume2)
        print(result)
    except ValueError as e:
        print(e)