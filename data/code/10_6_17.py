def compare_temperature(t1, t2):
    """
    Generates a comparison result between two temperature values.
    
    Yields messages indicating which value is higher and by how much.
    Handles edge cases like equal temperatures or invalid inputs (though 
    the problem implies valid numbers are provided).
    """
    if not isinstance(t1, (int, float)) or not isinstance(t2, (int, float)):
        yield f"Invalid input: both values must be numeric."
        return

    difference = t1 - t2
    
    if abs(difference) < 0.0001 and t1 != t2:
        # Floating point precision check for equality but distinct objects/strings? 
        # Simple float comparison is sufficient here as per standard usage unless specified otherwise.
        yield f"{t1} and {t2} are equal."
    elif difference > 0.0001:
        direction = "warmer" if t1 >= t2 else "cooler"
        magnitude = abs(difference)
        yield f"{t1} is {'more' if difference > 0 else 'less'} than {t2}. The difference is approximately {magnitude:.2f} degrees."
    elif difference < -0.0001:
        direction = "warmer" if t2 >= t1 else "cooler"
        magnitude = abs(difference)
        yield f"{t2} is {'more' if t2 > t1 else 'less'} than {t1}. The difference is approximately {magnitude:.2f} degrees."
    else:
        yield f"{t1} and {t2} are effectively equal (difference within 0.0001)."

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    temp_a = 75.5
    temp_b = 80.0
    
    print("Generating comparison results:")
    
    for result in compare_temperature(temp_a, temp_b):
        print(result)
        
    # Additional test case with same value
    print("\nTest case (equal values):")
    for result in compare_temperature(25, 25.0):
        print(result)