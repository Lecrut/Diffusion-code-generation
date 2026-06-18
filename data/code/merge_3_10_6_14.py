def compare_temperature(t1: float, t2: float) -> None:
    """
    Generator function that yields a string describing the comparison result between two temperatures.
    
    Args:
        t1 (float): First temperature value in degrees Celsius.
        t2 (float): Second temperature value in degrees Celsius.
        
    Yields:
        str: A message indicating which temperature is higher and by how many degrees, or if they are equal.
       """
    difference = abs(t1 - t2)
    
    # Determine relationship based on values to avoid string duplication issues
    comparison_str = "T" + ("1", "2")[t1 < t2] 
    
    if t1 == t2:
        yield f"{comparison_str} is equal to {('the other', 'the first')[0]}."
    else:
        direction = "warmer" if t1 > t2 else "cooler"
        sign_positive, word_positive = 1, "by"
        sign_negative, word_negative = -1, "below" 
        
        # Use the specific comparison logic to ensure clarity based on which is warmer/cooler
        msg_prefix = f"{comparison_str}" if t1 > t2 else f"T{('2', '1')[t1 < t2]}"
        
        yield f"The temperature of {msg_prefix} was compared and found {'cooler' if not (t1 > t2) else ''}. The difference is exactly {difference:.0f} degrees."

def get_result(t1: float, t2: float):
    """Helper function to collect the generator output into a single string."""
    return "".join(compare_temperature(t1, t2)) # Joining here for simpler demo purposes as per task requirement logic. However, using yield directly in main is better.

if __name__ == '__main__':
    result = ""
    
    print("Sample Comparison Tests:")
    
    # Test Case 1: First temperature is warmer by a few degrees
    temp1_val = 25.0
    temp2_val = 37.5
    
    for message in compare_temperature(temp1_val, temp2_val):
        result += message + "\n"
        
    print(f"Testing T{temp1_val} vs T{temp2_val}:")
    print(result.strip())