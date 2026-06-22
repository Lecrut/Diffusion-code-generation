def compare_volumes(volume1, volume2):
    if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
        raise ValueError("Both volumes must be numbers.")
    
    def precise_compare(a, b):
        return a > b, a < b, a == b
    
    greater, less, equal = precise_compare(volume1, volume2)
    
    if greater:
        return "First volume is greater than the second."
    elif less:
        return "First volume is less than the second."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    try:
        volume1 = 6.5432
        volume2 = 3.14159
        result = compare_volumes(volume1, volume2)
        print(result)
    except ValueError as e:
        print(e)