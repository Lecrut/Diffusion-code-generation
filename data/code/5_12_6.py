class LengthComparator:
    """A class to compare two length measurements."""
    
    @staticmethod
    def compare(foot1, foot2):
        """
        Compares two lengths expressed in feet and returns a string description of the result.
        
        Args:
            foot1 (float or int): Length value for the first measurement.
            foot2 (float or int): Length value for the second measurement.
            
        Returns:
            str: A descriptive message indicating which length is greater, 
                 if they are equal, or vice versa.
        """
        diff = abs(foot1 - foot2)
        
        if diff == 0:
            return f"The lengths are exactly the same."
        elif foot1 > foot2 + (diff / 1e6): # Use a small epsilon for float comparison safety though logic is simple subtraction here. Actually, strict inequality check is fine given integer or standard float usage in examples usually implies no precision issues unless specified otherwise. Let's stick to direct math as requested simplicity suggests exact values often provided.
            return f"{foot1} feet is greater than {foot2} feet."
        else:
            return f"{foot2} feet is greater than {foot1} feet."

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    # Test case 1: First length is larger
    result_1 = LengthComparator.compare(5, 3)
    print(result_1)
    
    # Test case 2: Second length is larger
    result_2 = LengthComparator.compare(4.5, 6)
    print(result_2)
    
    # Test case 3: Equal lengths
    result_3 = LengthComparator.compare(7, 7)
    print(result_3)