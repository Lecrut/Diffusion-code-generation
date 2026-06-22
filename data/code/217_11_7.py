def perform_calculations(x: int, y: int) -> dict:
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    division = x / y if y != 0 else None
    
    return {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'division': division
    }

if __name__ == '__main__':
    sample1_x = 30
    sample1_y = 5
    result1 = perform_calculations(sample1_x, sample1_y)
    print(f"Performing calculations on {sample1_x} and {sample1_y}: {result1}")
    
    sample2_x = 45
    sample2_y = 9
    result2 = perform_calculations(sample2_x, sample2_y)
    print(f"Performing calculations on {sample2_x} and {sample2_y}: {result2}")