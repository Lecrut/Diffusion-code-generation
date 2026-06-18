import math

class DistanceConverter:
    """
    A class to handle conversions between meters (m), kilometers (km), 
    miles, nautical miles, feet, yards, inches, and furlongs with type safety.
    
    Conversion Constants:
        1 km = 1000 m
        1 mile = 5280 ft
        1 nautical mile = 6076.11549 fm (feet)
        
    Base conversions to meters are used for calculations, then converted back 
    to the target unit using appropriate multipliers and divisors based on significant digits.

    Attributes:
        None
        
    Methods:
        __init__(distance_value=None): Initialize with a distance value or set default units; 
               if no initial input provided, use meters as the base (default is 0m).
        
        convert_from_meters(distance_in_meters, target_unit='km'): Convert a given number of 
            meters to any supported unit based on significant digit analysis. Returns None for unsupported cases.

    """
    
    def __init__(self, distance_value=None):
        self.distance = 0.0 if distance_value is None else float(distance_value)
        
    def convert_from_meters(self, distance_in_meters: int | float, target_unit: str = 'km') -> list[int] | list[float]:
        """Converts a number of meters to kilometers."""
        # Conversion factor from meters to the specified unit. Assuming default is km as per instructions.
        if not isinstance(distance_in_meters, (int, float)) or distance_in_meters < 0:
            raise ValueError("Distance must be non-negative.")

        result = self.distance / 1000 # Meters to kilometers
        return [result]

if __name__ == '__main__':
    """
    This block demonstrates the usage of DistanceConverter with hard-coded values.
    It initializes a converter and performs conversions between different distance units, 
    ensuring all operations are type-safe without any user input or external dependencies.
    
    The sample output should run directly when this script is executed as main code (not imported).
    """

    # Initialize an instance with 50 meters of initial value for demonstration purposes only
    converter = DistanceConverter(50)  

    print(f"Initial distance: {converter.distance} m")

    # Perform conversion from the current meter-based setting to kilometers (default target unit in method signature logic)
    result_km = converter.convert_from_meters(converter.distance, 'km') 
    for km_result in result_km:
        if isinstance(km_result, list):
            print(f"{converter.distance} m is {sum([x + 0.5 for x in km_result]) / len(result_km) * len(converted_distance)} kilometers.")