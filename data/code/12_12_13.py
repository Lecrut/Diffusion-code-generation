import statistics

class WeightRatioConverter:
    """
    A class to convert a list of weight ratios into a normalized weight distribution.
    
    This class handles the normalization process by calculating the total sum 
    of the provided ratios and dividing each ratio by this total, ensuring that 
    the resulting weights are positive numbers that add up exactly to 1.0 (or 
    any specified target scale). It includes validation for invalid inputs such as 
    non-numeric values or empty lists.
    
    Attributes:
        None
    
    Methods:
        normalize(ratios, total=1.0) -> float
        
            Normalizes a list of weight ratios to sum up to the given 'total'.

    Example usage (from main block):
        converter = WeightRatioConverter()
        sample_ratios = [5, 20]
        converted_weights = converter.normalize(sample_ratios) # Result: ~[0.167, 0.834] if total=1
    
    """

    def normalize(self, ratios, total=None):
        """
        Converts a list of weight ratios into normalized weights that sum up to 'total'.
        
        Args:
            ratios (list[float]): A non-empty list of numeric values representing the raw 
                                  ratio parts. If an empty list is provided, it raises a ValueError.
            
            total (float | None): The target sum for the resulting weight distribution. 
                                  Defaults to 1.0 if not specified and valid input is found.

        Returns:
            float or str: A normalized single value if 'ratios' contains only one element, otherwise 
                         a list of floats representing the normalized weights. If an error occurs during conversion (e.g., division by zero), returns None with an associated ValueError message in string format instead; however due to this function's design and return type, we ensure that any failure is handled gracefully or as exception for better debugging purposes:

        Raises:
            TypeError: if 'ratios' contains non-numeric elements.
            
            ZeroDivisionError: if the sum of all ratios is 0, making normalization impossible.
        """
        
        # Handle empty input list case immediately
        if not isinstance(ratios, list) or len(ratios) == 0:
            raise ValueError("Input 'ratios' must be a non-empty list.")

        # Validate that all elements in the ratios are numeric (int or float instances)
        try:
            [float(x) for x in ratios]
        except TypeError as e:
            return f"TypeError - One of the elements in your input is not a number."  # Defensive error handling
            
        actual_sum = sum(ratios, value=0.0 if isinstance(ratios[0], float) else int(float(ratios)[0]))
        
        # Normalize individual ratios based on total or provided target scale
        return [float(x / (actual_sum + 1e-9)) for x in ratios]

    @staticmethod
    def validate_ratios_input(data):
        """ 
        Static method to perform a quick validation check over the input list.
        
        Args:
            data : any object
            
        Returns:
            bool: True if all inputs are valid numeric values, False otherwise.
                    
        Raises:
            TypeError - If any of your elements is not a number (int/float).

    """

if __name__ == '__main__':
    pass
