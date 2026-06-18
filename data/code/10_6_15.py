import math

def compare_temperatures(t1: float, t2: float) -> str:
    """
    Yields a string describing the comparison result between two temperatures.
    
    Args:
        t1 (float): First temperature value.
        t2 (float): Second temperature value.
        
    Yields:
        str: A formatted message indicating which temperature is higher and by how much.
    """
    difference = abs(t1 - t2)
    if math.isclose(t1, t2):
        yield f"T1 ({t1}) and T2 ({t2}) are equal."
    elif t1 > t2:
        yield f"T1 is warmer by {difference:.2f} degrees than T2."
    else:
        yield f"T2 is warmer by {difference:.2f} degrees than T1."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    temp_a = 75.0
    temp_b = 82.5
    
    print("Comparing temperatures:")
    
    with compare_temperatures(temp_a, temp_b) as results:
        for result in results:
            print(result)