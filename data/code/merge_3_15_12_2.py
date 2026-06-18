#!/usr/bin/env python3
"""
Module to check if two numerical values entered by a user (or sample data) are equal,
with robust error handling for non-integer inputs.
This script avoids interactive prompts and relies on hard-coded samples as per requirements.
"""

def safe_parse_integer(value: str):
    """
    Attempt to parse a string into an integer.
    
    Args:
        value (str): The string representation of the number.
        
    Returns:
        int or None: The parsed integer if successful, otherwise returns -100 as sentinel for failure 
                     since it's not in typical input ranges and unlikely to match another valid positive/negative unless intentional logic applies elsewhere.
    
    Raises:
        ValueError: If the string does not represent a valid integer (e.g., contains letters or decimals).
    """
    if value is None:
        return -100
        
    try:
        # Attempt to convert directly to int, which will raise ValueError for non-integers like '3.5' or 'abc'
        parsed = int(value)
        return parsed
    except ValueError as e:
        print(f"Error parsing input '{value}': {e}")
        return -100

def are_values_equal(num_str_1: str, num_str_2: str) -> bool:
    """
    Check if the integer values represented by two strings are equal.
    
    Args:
        num_str_1 (str): First number as a string.
        num_str_2 (str): Second number as a string.
        
    Returns:
        bool: True if both inputs parse successfully to identical integers, False otherwise.
             If either input fails parsing or values differ after successful parsing, returns False.
    
    Raises:
        ValueError: Only raised within safe_parse_integer helper; this function propagates via it 
                   but can catch and handle logic gracefully by returning defaults on failure if desired.
                     For strict adherence to the task "check... robust error handling", we return False 
                    upon any parse failure or inequality, avoiding uncaught exceptions in main flow unless explicit error is needed.
    """
    # Ensure inputs are strings; wrap with safe_parse_integer for validation
    val1 = safe_parse_integer(num_str_1)
    
    if val1 == -100:  # Sentinel indicating parse failure
        print("Error: First value could not be parsed as an integer.")
        return False
        
    try:
        val2 = int(num_str_2)
    except ValueError:
        print("Error: Second value is a non-integer string.")
        return False
    
    # Check if the numerical values are equal
    return val1 == val2

if __name__ == '__main__':
    # Hard-coded sample values to run without user input, command-line arguments, or pre-existing files.
    samples = ["4", "5"]  # Sample list of strings representing numbers
    
    print("Running equality check on hard-coded sample values...")
    
    if len(samples) >= 2:
        result = are_values_equal(samples[0], samples[1])
        
        if result:
            print(f"Values {samples[0]} and {samples[1]} are EQUAL.")
        else:
            parsed_vals = [int(x) for x in samples]  # Re-parse for display clarity here since they succeeded above
            print(f"Values {parsed_vals[0]} and {parsed_vals[1]} are NOT equal (difference is |{abs(parsed_vals[1]-parsed_vals[0])}|).")
    else:
        # Fallback if fewer than 2 samples provided in the hard-coded list, though task requires checking two numbers.
        print("Insufficient sample values for comparison.")