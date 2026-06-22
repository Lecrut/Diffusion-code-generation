def validate_yard_inches(yards, inches):
    if not isinstance(yards, (int, float)) or not isinstance(inches, int) or inches < 0:
        raise ValueError("Invalid input: yards must be a number and inches must be a non-negative integer")

def compare_measures(y1, i1, y2, i2):
    validate_yard_inches(y1, i1)
    validate_yard_inches(y2, i2)
    
    total_inches1 = y1 * 36 + i1
    total_inches2 = y2 * 36 + i2
    
    if total_inches1 < total_inches2:
        return f"{y1} yards {i1} inches"
    elif total_inches2 < total_inches1:
        return f"{y2} yards {i2} inches"
    else:
        return "Both measures are equal"

if __name__ == '__main__':
    result = compare_measures(5, 8, 4, 30)
    print(result)