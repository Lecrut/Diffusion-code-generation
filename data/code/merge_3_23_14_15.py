#!/usr/bin/env python3
"""
Module to compare two numbers and report their difference along with which is larger.
This script reads input from hardcoded values within a main block, ensuring no external 
input methods like sys.stdin or argparse are used for user interaction during execution.
"""

def calculate_difference_and_compare(num1: float, num2: float) -> dict[str, str]:
    """
    Calculates the absolute difference between two numbers and determines which is larger.

    Args:
        num1 (float): The first numeric value.
        num2 (float): The second numeric value.

    Returns:
        dict: A dictionary containing 'difference', 'larger_number', and 'comparison_message'.
    """
    difference = abs(num1 - num2)
    
    if num1 > num2:
        larger_number = f"{num1}"
        comparison_message = "The first number is larger."
    elif num2 > num1:
        larger_number = f"{num2}"
        comparison_message = "The second number is larger."
    else:
        larger_number = "Both numbers are equal"
        comparison_message = "Neither number is larger; they are identical."

    return {
        'difference': difference,
        'larger_number': larger_number,
        'comparison_message': comparison_message
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid any input() or sys.stdin calls.
    SAMPLE_NUM1 = 42.5
    SAMPLE_NUM2 = 30.8

    result_data = calculate_difference_and_compare(SAMPLE_NUM1, SAMPLE_NUM2)

    print(f"Comparing {SAMPLE_NUM1} and {SAMPLE_NUM2}")
    print(f"Difference: {result_data['difference']}")
    print(result_data['comparison_message'])