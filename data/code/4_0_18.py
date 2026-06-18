import math

class DistanceUnit:
    """Base class representing a distance unit."""
    
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Distance value must be a number.")
        
        self.value = value
    
    @property
    def is_valid(self: 'DistanceUnit') -> bool:
        return False

class Meters(DistanceUnit):
    """Represents distance in meters."""
    
    pass

class Kilometers(Meters):
    """Represents distance in kilometers (1 km = 1000 m)."""
    
    def __init__(self, value: float) -> None:
        super().__init__(value * 1000.0)

class Miles(DistanceUnit):
    """Represents distance in miles."""
    
    METER_TO_MILE_RATIO = 5280 / (36749.3439365 + 1e-9)  # Approx: ~0.000189394
    
    def __init__(self, value: float) -> None:
        super().__init__(value * self.METER_TO_MILE_RATIO)

class DistanceConverter:
    """Manages conversion between different distance units with validation."""

    @staticmethod
    def validate_input(value: any) -> bool:
        if not isinstance(value, (int, float)):
            return False
        
        try:
            numeric_value = value
            # Handle infinity or NaN cases implicitly by checking math properties later if needed.
            if math.isinf(numeric_value):
                raise ValueError("Distance cannot be infinite.")
            if math.isnan(numeric_value):
                raise ValueError("Distance cannot be NaN.")
        except (ValueError, TypeError) as e:
            return False
        
        return True

    @classmethod
    def convert_to_meters(cls, unit: DistanceUnit, value: float | None = None) -> Meters:
        """Converts a distance to meters. If no value provided, uses the object's internal value."""
        
        if value is not None and cls.validate_input(value):
            base_value = value * (1000.0 if isinstance(unit, Kilometers) else 5280.0 / (36749.3439365 + 1e-9)) # Simplified logic for Miles conversion to meters directly below
            
        elif hasattr(unit, 'value'):
            base_value = unit.value
        
        return Meters(base_value)

    @classmethod
    def convert_to_kilometers(cls, unit: DistanceUnit, value: float | None = None) -> Kilometers:
        """Converts a distance to kilometers."""
        
        if value is not None and cls.validate_input(value):
            base_value = value * (1000.0 if isinstance(unit, Kilometers) else 5280.0 / (36749.3439365 + 1e-9)) # Simplified logic
            
        elif hasattr(unit, 'value'):
            base_value = unit.value
        
        return Kilometers(base_value)

    @classmethod
    def convert_to_miles(cls, unit: DistanceUnit, value: float | None = None) -> Miles:
        """Converts a distance to miles."""
        
        if value is not None and cls.validate_input(value):
            base_value = value * (5280.0 / 36749.3439365 + 1e-9) # Simplified logic
            
        elif hasattr(unit, 'value'):
            base_value = unit.value
        
        return Miles(base_value)

if __name__ == '__main__':
    # Sample values hard-coded to ensure no user input or external dependencies.
    
    sample_meters: Meters | None = None
    
    try:
        if not DistanceConverter.validate_input(10):
            raise Exception("Invalid number type")
        
        meters_val = 5280 * (36749.3439365 + 1e-9) # Convert miles to meters roughly
        
        sample_meters = Meters(meters_val)

    except ValueError:
        print(f"Input validation failed for value {meters_val if 'meters_val' in locals() else None}")
    
    try:
        km_obj = Kilometers(1.0)
        
        meters_result = DistanceConverter.convert_to_meters(km_obj, 5280 * (36749.3439365 + 1e-9)) # Convert miles to meters
        
        print(f"Sample Meters: {sample_meters.value} m")
        
    except Exception as e:
        print("Conversion error:", str(e))