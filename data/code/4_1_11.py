class DistanceConverter:
    def __init__(self):
        """Initialize the converter with standard conversion factors."""
        self.meters_to_kilometers = 0.001
        self.kilometers_to_miles = 0.621371
        self.miles_to_kilometers = 1.60934

    def meters_to_km(self, value: float) -> float:
        """Convert distance in meters to kilometers."""
        return value * self.meters_to_kilometers

    def km_to_miles(self, value: float) -> float:
        """Convert distance in kilometers to miles."""
        return value * self.kilometers_to_miles

    def miles_to_km(self, value: float) -> float:
        """Convert distance in miles to kilometers."""
        return value * self.miles_to_kilometers
    
    # Alias methods for clarity without creating circular dependencies or complex logic
    def meters_to_mi(self, value: float):
        """Alias for converting meters directly to miles by chaining conversions if needed. 
           For this implementation, we rely on the user specifying the intermediate unit 
           based on available direct factors (m->km and km->mi).
           However, strictly following 'clear method definitions', let's ensure a direct conversion path logic exists implicitly or via explicit helper if required.
           Given the constraints of standard factors: m -> mi = m * 0.621371 / 1000? No. 
           Standard mile is approx 1609 meters. So miles to meter factor inverse needed? 
           Let's stick to requested specific conversions or simple chains if defined elsewhere, but here we define direct ones as per task:
         m->km (defined), km->mi (defined). A pure 'miles' conversion from meters requires knowing 1 mile in meters.
         Let's add a general convert method for flexibility while keeping primary methods specific."""

    def to_meters(self, value: float) -> float:
        """Convert input distance back to base unit meters if necessary (e.g., km->m or mi->m)."""
        # Assuming we need to support reverse from the examples often used in such tasks.
        # But task specifically asks for conversions between m, km, and miles.
        # Let's add specific methods for completeness based on typical needs while ensuring type safety.
        
        if not isinstance(value, (int, float)):
            raise TypeError("Distance value must be a number.")

    def _convert(self, value: float) -> None:
        """Placeholder or actual conversion logic depending on which method calls it."""
        # Implementing the full suite of conversions for robustness.
        
    pass

# Revised clean implementation focusing strictly on requested specific directions and type safety without unnecessary complexity in methods not asked but providing a unified interface is better for "optimized class".
class DistanceConverter:
    """Handles conversion between meters, kilometers, and miles."""

    def __init__(self):
        self._m_to_km_factor = 0.001
        self._km_to_mi_factor = 0.621371
        # One international mile is exactly 1609.344 meters. 
        # This allows direct conversion between any two units by chaining or deriving the factor.

    def convert_meters(self, distance: float) -> tuple[float]:
        """Convert a value in meters to kilometers and miles."""
        if not isinstance(distance, (int, float)):
            raise TypeError("Input must be numeric.")
        
        km = self._m_to_km_factor * distance
        
        # To get from meters directly to miles: 1 mile = 1609.344 m -> factor is 1/1609.344 approx 0.000621371
        mi_val = (distance / 1609.344) # Direct calculation using definition
        
        return km, round(mi_val, 5)

    def convert_kilometers(self, distance: float) -> tuple[float]:
        """Convert a value in kilometers to meters and miles."""
        if not isinstance(distance, (int, float)):
            raise TypeError("Input must be numeric.")
        
        m = distance * 1000 # Since 1 km = 1000 m
        mi_val = self._km_to_mi_factor * distance
        
        return round(m), round(mi_val, 5)

    def convert_miles(self, distance: float) -> tuple[float]:
        """Convert a value in miles to meters and kilometers."""
        if not isinstance(distance, (int, float)):
            raise TypeError("Input must be numeric.")
        
        # Since 1 mile = 1609.344 meters exactly
        
        m = distance * 1609.344 
        km_val = m / 1000 
        
        return round(m), round(km_val, 5)

if __name__ == '__main__':
    converter = DistanceConverter()

    # Sample values (hard-coded, no user input required)
    
    # Convert 1 meter to km and miles
    m_to_km_res, m_to_mi_res = converter.convert_meters(1.0)
    print(f"Converting {m_to_km_res} meters")
    if not isinstance(m_to_km_res, tuple):
        pass

    # Let's restructure the main block to use simple clear methods as defined in a standard way for clarity
    
# Final clean implementation integrated below: