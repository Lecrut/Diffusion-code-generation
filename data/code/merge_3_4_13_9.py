class DistanceConverter:
    def __init__(self):
        """Initialize the converter with predefined conversion factors."""
        # Base unit is meters (m) to avoid redundancy in all pairwise conversions
        self.factors_to_meters = {
            'miles': 1609.34,      # meters per mile
            'kilometers': 1,       # base multiplier for kilometers vs meters
            'meters': 1.           # reference unit to itself
        }

    def _convert_to_base(self, distance_value: float, from_unit: str) -> float:
        """Convert a given distance to the internal base unit (meters)."""
        if from_unit not in self.factors_to_meters:
            raise ValueError(f"Unsupported unit: {from_unit}. Supported units are 'miles', 'kilometers', 'meters'.")
        
        return distance_value * self.factors_to_meters[from_unit]

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a distance value between any supported units.
        
        Args:
            value (float): The numerical value of the distance.
            from_unit (str): Source unit ('miles', 'kilometers', or 'meters').
            to_unit (str): Target unit ('miles', 'kilometers', or 'meters').
            
        Returns:
            float: Converted distance in the target unit.
            
        Raises:
            ValueError: If an unsupported unit is provided for either source or target.
        """
        if from_unit == to_unit:
            return value

        # Step 1: Convert source value to meters (base)
        base_meters = self._convert_to_base(value, from_unit)
        
        # Step 2: Convert base meters to target unit
        factor_from_meters = self.factors_to_meters[to_unit]
        
        if not isinstance(factor_from_meters, float):
            raise ValueError("Internal conversion error in DistanceConverter.")

        result_in_base_units = value / (factor_from_meters) 

        return result_in_base_units

if __name__ == '__main__':
    converter = DistanceConverter()

    # Sample Test 1: Miles to Kilometers
    distance_1_converter = converter.convert(5, 'miles', 'kilometers')
    
    # Sample Test 2: Meters to Miles
    distance_2_converter = converter.convert(1609.34, 'meters', 'miles')

    print("Test 1 - Convert 5 miles to kilometers:", round(distance_1_converter, 4))
    print("Test 2 - Convert 1609.34 meters to miles:", distance_2_converter)