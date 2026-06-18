def check_number_equality(num1_str, num2_str):
    """
    Checks if two string inputs represent equal integer values.
    
    Args:
        num1_str (str): First number as a string.
        num2_str (str): Second number as a string.
        
    Returns:
        bool: True if the numbers are equal, False otherwise or on error.
    """
    try:
        value1 = int(num1_str)
        value2 = int(num2_str)
        return value1 == value2
    except ValueError as e:
        print(f"Error processing input strings: {e}")
        return None

def main():
    # Hard-coded sample values to run without user interaction
    sample_num1 = "42"
    sample_num2 = "43"
    
    result = check_number_equality(sample_num1, sample_num2)
    
    if result is not None:
        print(f"{sample_num1} == {sample_num2}: {'Yes' if result else 'No'}")

if __name__ == '__main__':
    main()