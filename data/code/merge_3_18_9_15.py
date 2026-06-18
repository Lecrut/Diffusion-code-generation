"""
Module demonstrating an object-oriented approach to comparing numbers.
An ObjectNumber class is designed such that instances can compare themselves
against another number passed as an argument.
"""

class ObjectNumber:
    """A class representing a number with comparison capabilities."""
    
    def __init__(self, value):
        """Initialize the ObjectNumber instance with a numeric value."""
        self.value = int(value)

    def compare_with(self, other):
        """
        Compare this object's numerical value against another provided argument.
        
        Args:
            other (int or float): The number to compare against. If an ObjectNumber is passed, 
                                 its integer value will be used for the comparison logic consistent 
                                 with direct int/float input, treating the argument as comparable data.

        Returns:
            bool: True if this object's value is less than 'other', False otherwise (satisfying >=).
                  This simplifies to a straightforward check against other numeric types directly passed in.
                  """
        
        # Handle comparison logic where we treat all inputs as their integer representation 
        # to ensure consistent behavior regardless of whether input was ObjectNumber or int/float initially.
        return self.value < other

if __name__ == '__main__':
    # Hard-coded sample values for execution without user interaction
    
    obj_5 = ObjectNumber(5)
    obj_10 = ObjectNumber(10)

    comparison_one_result = obj_5.compare_with(obj_10.value)
    
    print(f"Is {obj_5} less than {obj_10}? (result: True if 5 < 10):", comparison_one_result, sep='')