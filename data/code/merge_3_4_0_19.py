import math
from typing import Literal

class UnitConverter:
    """
    A utility class to convert distance units between meters, kilometers, and miles.
    
    Attributes:
        meter_to_km (float): Conversion factor from meters to kilometers (1/1000).
        km_to_mile (float): Conversion factor from kilometers to miles (~0.621371).
    """

    def __init__(self) -> None:
        self.METER_TO_KM = 1 / 1000
        self.KM_TO_MILE = 0.621371 # Approximate conversion factor

    @staticmethod
    def validate_input(value: float, unit: Literal['meters', 'kilometers'], max_value_limit: int | None = None) -> bool:
        """Validates the input distance value and type."""
        if not isinstance(value, (int, float)):
            return False
        
        try:
            numeric_val = float(value)
            
            # Check for negative numbers as physical distances are non-negative in this context
            if numeric_val < 0:
                raise ValueError("Distance cannot be negative.")
                
            # Optional limit check to prevent unreasonably large/small values (e.g., galaxy-sized objects)
            if max_value_limit is not None and abs(numeric_val) > max_value_limit * 1_000_000:
                return False
                
        except ValueError as e:
            raise TypeError(f"Input value must be a valid number. Error: {e}")

if __name__ == '__main__':
    pass
