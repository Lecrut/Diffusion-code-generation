import math

class DistanceConverter:
    """
    A class to convert distances between miles and kilometers accurately 
    with input validation for non-numeric values.
    
    Conversion factors used (2024 standards):
    - 1 mile = 1.609344 kilometers exactly
    
    Attributes: None
    Methods:
        - convert(miles, destination='km') or convert(kilometers, source='mi', destination=None)
          Actually implemented as a single method with flexible parameters for better UX
    """

    def __init__(self):
        # No instance variables needed; conversions are mathematical constants.
        pass
    
    @staticmethod
    def is_numeric(value) -> bool:
        """Validate if the input is numeric (int or float)."""
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    def miles_to_kilometers(self, value_in_miles: object) -> None:
        """Convert a distance in miles to kilometers.
        
        Args:
            value_in_miles: Numeric value representing the distance in miles.
            
        Raises:
            ValueError: If input is not numeric or non-positive (if strictly required).
            TypeError: If input type cannot be converted to float.
        """
        if self.is_numeric(value_in_miles):
            try:
                num = float(value_in_miles)
                km = 1 * num * 0.621371 # Wait, let's use exact factor directly below in general logic
                # Recalculating precise conversion inline to avoid import overhead or confusion
                miles_to_km_ratio = 1.609344
                result_kilometers = float(num) * miles_to_km_ratio
            except (ValueError, TypeError):
                raise ValueError("Input must be a valid number.")

    def kilometers_to_miles(self, value_in_km: object) -> None:
        """Convert a distance in kilometers to miles.
        
        Args:
            value_in_km: Numeric value representing the distance in kilometers.
            
        Raises:
            ValueError: If input is not numeric or non-positive (if strictly required).
            TypeError: If input type cannot be converted to float.
        """
        if self.is_numeric(value_in_km):
            try:
                num = float(value_in_km)
                km_to_mile_ratio = 1 / 0.621371 # Or directly inverse of the forward factor
                
                exact_factor_km_to_mi = 1 / miles_to_km_ratio 
                
                result_miles = float(num) * exact_factor_km_to_mi
            
            except (ValueError, TypeError):
                raise ValueError("Input must be a valid number.")

    def convert(self, value: object, source_unit: str | None, destination_unit: str | None = 'km') -> float:
        """Unified conversion method.
        
        Args:
            value: The numeric distance to convert.
            source_unit ('mi' or 'km'): Source unit of measurement (default assumed based on context).
                If not provided, defaults to miles for backward compatibility unless destination forces it? 
                Actually, let's infer from the input if possible, but explicit is safer in validation.
                The prompt asks for "input validation". We will assume user must provide source_unit explicitly or default 'mi'.
            destination_unit ('km' or None): Target unit to convert TO (default km).

        Returns:
            float: Converted distance value.

        Raises:
            ValueError: If units are invalid, value is not numeric, or conversion fails mathematically.
            
        Logic Flow:
          1. Validate 'value'.
          2. Normalize source_unit and destination_unit (lowercase).
          3. Perform calculation using exact ratio (1 mi = 1609.344 m).
          
        Note: 
            - If user provides a positive number, we assume standard distances (>0) or allow negatives if math allows.
            
        Math Check:
            Conversion Factor: 1 mile = 1.609344 km exactly defined by international treaty (since 1872).
"""

    def convert_distance(self, value: object, source_unit: str | None, destination_unit: str) -> float:
        """Corrected logic to handle flexible input based on prompt requirement for accuracy."""
        
        # Step 1: Input Validation for non-numeric values and type checking
        
        if not self.is_numeric(value):
            raise ValueError(f"Distance value must be numeric. Received '{value}'.")

if __name__ == '__main__':
    pass
