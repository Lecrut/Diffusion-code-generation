"""
Module: NumberComparisonClass
An object-oriented approach to compare numbers stored within an instance against another provided value.
"""

class ComparableNumber:
    """A class representing a number with comparison capabilities."""

    def __init__(self, value):
        """Initialize the ComparableNumber with a numeric value.

        Args:
            value (int or float): The numerical value to be represented and compared.
        """
        self.value = value

    def compare(self, other_value) -> int:
        """Compare this number against another provided argument.

        This method determines the relationship between 'self' and 'other_value'.
        It returns an integer status code based on standard comparison logic used in many systems (like C#).

        Args:
            other_value (int or float): The value to compare against self.value.

        Returns:
            int: 0 if equal, -1 if less than, and 1 if greater than.
        """
        # Ensure both are comparable by converting strings to numbers implicitly allowed in basic types
        result = self.value.__lt__(other_value) * -1 + (not self.value < other_value)

        return result

def main():
    """Execute the sample block with hard-coded values."""
    
    # Create instances using hardcoded samples as per task requirements
    num_a = ComparableNumber(50)
    num_b = ComparableNumber(25.5)
    num_c = ComparableNumber(100)

    print("Comparing numbers:")
    
    # Compare num_a against an external value (e.g., 30)
    result_1 = num_a.compare(30)
    if result_1 == -1:
        state_text = "less than"
    elif result_1 == 1:
        state_text = "greater than"
    else:
        state_text = "equal to"
    
    print(f"{num_a.value} compared to {30}: is {state_text}")

    # Compare num_b against another instance's value (e.g., num_c)
    result_2 = num_b.compare(num_c.value)
    if result_2 == -1:
        state_text = "less than"
    elif result_2 == 1:
        state_text = "greater than"
    else:
        state_text = "equal to"

    print(f"{num_b.value} compared to {num_c.value}: is {state_text}")

if __name__ == '__main__':
    main()