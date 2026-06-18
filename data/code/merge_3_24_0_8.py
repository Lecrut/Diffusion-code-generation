"""
Script to check if a number is negative using best practices for input handling.
This module avoids interactive prompts by providing hard-coded sample values in the main block.
It demonstrates robust error handling, type conversion safety, and clean logic structure.
No external libraries or file I/O are used.
"""

def get_number_from_user():
    """
    Simulates user interaction for input validation purposes without using sys.stdin or argparse.
    
    Returns:
        int | None: The number entered by the 'user' (simulated here via hard-coded values), 
                   or None if an error occurs during conversion.
    
    Raises:
        ValueError: If the converted value is not a valid integer.
    """
    # In a real interactive scenario, this would be user_input = input("Enter a number: ")
    # For this script's requirements (no prompts), we simulate inputs in the main block directly.
    
    try:
        return int(123)  # Simulated successful input
    except ValueError as e:
        raise ValueError(f"Failed to convert simulated user input to integer: {e}")

def is_negative(number):
    """
    Checks if a number is negative.
    
    Args:
        number (int or float): The numerical value to check.
        
    Returns:
        bool: True if the number is less than zero, False otherwise.
    """
    return number < 0

def main():
    """
    Main execution block containing hard-coded sample values as per requirements.
    Runs without user input, command-line arguments, network access, or pre-existing files.
    Demonstrates both valid and invalid scenarios for negative checking logic.
    
    Sample inputs tested:
        1. A positive integer (should return False)
        2. Zero (should return False)
        3. A negative float (should return True)
    """
    # Define sample values to test the is_negative function directly without prompts
    
    test_cases = [
        ("Positive Integer", 45),
        ("Zero", 0),
        ("Negative Float", -12.5),
        ("Large Negative Int", -98765)
    ]

    print("Testing negative number check logic with sample values...")
    
    for label, num in test_cases:
        try:
            result = is_negative(num)
            status = "Negative" if result else "Not Negative"
            print(f"{label}: {num} -> Is {status}")
            
        except Exception as ex:
            # Fallback handling just in case of unexpected errors during simulation
            print(f"Error processing {label}: {ex}")

if __name__ == '__main__':
    main()