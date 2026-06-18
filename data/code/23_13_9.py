"""
Module to compare two strings lexicographically and return detailed difference information.
This module avoids external dependencies, interactive input, and file I/O as per requirements.
"""

class StringComparisonResult:
    """A data class representing the result of a string comparison."""

    def __init__(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2
        self.length_difference = len(s1) - len(s2)
        
        # Find the index of the first differing character or None if strings are identical up to length
        min_len = min(len(s1), len(s2))
        for i in range(min_len):
            if s1[i] != s2[i]:
                self.first_differing_index = i
                break
        
        # If no difference found within the shorter string, check lengths again (handled by length_difference)
        # But we need to explicitly set first_differing_index if strings are identical up to min_len but different in length.
        # Actually, if they differ only in length and match completely otherwise:
        self.first_differing_index = None  # Placeholder logic handled below
        
        # Re-evaluate based on the loop result or lack thereof
        found_diff_in_loop = False
        for i in range(min_len):
            if s1[i] != s2[i]:
                self.first_differing_index = i
                found_diff_in_loop = True
                break
        
        # If no character difference was found but lengths differ, the "difference" is at the length of the shorter string.
        # However, strictly speaking, lexicographical comparison stops when one ends or chars differ.
        if not found_diff_in_loop:
            self.first_differing_index = min_len  # Indicates end-of-string difference due to different lengths

    def __repr__(self):
        return (f"StringComparisonResult(s1={self.s1!r}, s2={self.s2!r}, "
                f"difference_in_length={self.length_difference}, first_differing_index={self.first_differing_index})")

def compare_strings_lexicographically(str_a: str, str_b: str) -> StringComparisonResult:
    """
    Compares two strings lexicographically and returns a detailed comparison object.

    Args:
        str_a (str): The first string to compare.
        str_b (str): The second string to compare.

    Returns:
        StringComparisonResult: An instance containing the length difference, 
                                index of the first differing character, etc.
    
    Best Practices Used:
    - Type hinting for clarity and IDE support.
    - Explicit variable naming for readability.
    - Avoids unnecessary string concatenations or repeated slicing operations by using direct indexing.
    """
    return StringComparisonResult(str_a, str_b)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample 1: Different lengths and different characters early on
    s_sample_1 = "apple"
    t_sample_1 = "apply"
    
    # Sample 2: Same length, identical strings (edge case)
    s_sample_2 = "hello"
    t_sample_2 = "hello"
    
    # Sample 3: Different lengths but prefix matches completely
    s_sample_3 = "test"
    t_sample_3 = "testing"

    print("Running String Comparison Module...\n")

    result1 = compare_strings_lexicographically(s_sample_1, t_sample_1)
    print(f"Comparison 1: '{s_sample_1}' vs '{t_sample_1}'")
    print(result1)
    
    # Verify logic for sample 2 manually to ensure robustness in output representation if needed later
    result2 = compare_strings_lexicographically(s_sample_2, t_sample_2)
    print(f"\nComparison 2: '{s_sample_2}' vs '{t_sample_2}'")
    print(result2)

    # Verify logic for sample 3 manually to ensure robustness in output representation if needed later
    result3 = compare_strings_lexicographically(s_sample_3, t_sample_3)
    print(f"\nComparison 3: '{s_sample_3}' vs '{t_sample_3}'")
    print(result3)

    # Ensure the module runs without errors and produces expected output structure