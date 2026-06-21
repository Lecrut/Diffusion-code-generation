def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers")
    
    comparison_results = {
        1: "Volume 1 is larger",
        -1: "Volume 2 is larger",
        0: "Volumes are equal"
    }
    
    return comparison_results[(volume1 > volume2) - (volume1 < volume2)]

if __name__ == '__main__':
    volume1 = 100.0
    volume2 = 200.0
    try:
        result = compare_volumes(volume1, volume2)
        print(result)
    except ValueError as e:
        print(e)