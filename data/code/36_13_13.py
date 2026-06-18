#!/usr/bin/env python3
"""
Standalone Python program to reverse a sentence.
Prompts user input (simulated with sample values in main block) 
and displays the reversed string using efficient slice manipulation.
"""

def reverse_sentence(text: str) -> str:
    """
    Reverses the given text efficiently by slicing from end to start step -1.

    Args:
        text (str): The input sentence or string to be reversed.

    Returns:
        str: A new string containing characters of 'text' in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user interaction needed here.
    SAMPLE_INPUT_1 = "Hello, World!"
    SAMPLE_INPUT_2 = "Python is great for learning."

    print("Sample 1: Input:", repr(SAMPLE_INPUT_1))
    reversed_result_1 = reverse_sentence(SAMPLE_INPUT_1)
    print("Reversed Output:", reversed_result_1)
    
    print("\n")

    print("Sample 2: Input", repr(SAMPLE_INPUT_2))
    reversed_result_2 = reverse_sentence(SAMPLE_INPUT_2)
    print("Reversed Output:", reversed_result_2)