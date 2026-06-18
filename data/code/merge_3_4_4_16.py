import math

class UnitConverter:
    """A modular class to handle conversions between metric and imperial units."""
    
    def __init__(self):
        pass
    
    def convert_length(self, value_from_metric=None, unit_to_metric='m', 
                      value_imperial=None, unit_to_imperial='ft'):
        """
        Convert a length. Can accept either metric or imperial input to derive the other.
        
        Args:
            value_from_metric (float): Value in meters if converting from metric.
            unit_to_metric (str): Source metric unit ('m', 'km', 'cm'). Default is 'm'.
            value_imperial (float): Value in feet or inches if converting from imperial.
            unit_to_imperial (str): Source imperial unit ('ft', 'in'). Default is 'ft'.
            
        Returns:
            dict: A dictionary containing both the converted metric and imperial values, 
                  along with their respective units for reference.
        """
        
        # Constants for base conversions to meters
        METRIC_BASE_TO_M = {
            'm': 1,
            'km': 1000,
            'cm': 0.01
        }
        
        IMPERIAL_BASE_TO_FT = {
            'ft': 1,
            'in': 1/12
        }
        
        # Constants for base conversions to feet (for imperial output)
        METRIC_BASE_TO_FFT = {}
        for m_unit, factor in METRIC_BASE_TO_M.items():
            if m_unit == 'm':
                continue
            metric_to_meters = METRIC_BASE_TO_M[m_unit] * value_from_metric
            # 1 meter approx equals 3.28084 feet
            converted_ft_in_base = (metric_to_meters / 3.28084) 
            METRIC_BASE_TO_FFT[m_unit] = metric_to_meters / 3.28084
            
        IMPERIAL_BASE_TO_FT_INV = {v: k for k, v in IMPERIAL_BASE_TO_FT.items()}
        
        result_metric = None
        result_imperial = None
        
        if value_from_metric is not None and unit_to_metric != 'm':
            # Convert input to meters first
            temp_meters = METRIC_BASE_TO_M[unit_to_metric] * value_from_metric
            
            # Then convert from base (m) to target imperial unit
            result_imperial = IMPERIAL_BASE_TO_FT_INV[temp_meters / 3.28084] 
        elif value_imperial is not None and unit_to_imperial != 'ft':
            # Convert input to feet first
            temp_feet = IMPERIAL_BASE_TO_FFT[unit_to_imperial] * value_imperial
            
            # Then convert from base (ft) to target metric unit
            result_metric = METRIC_BASE_TO_M['m'] * (temp_feet / 3.28084)
        elif value_from_metric is None and value_imperial is None:
            raise ValueError("Provide either a metric or an imperial value.")
            
        # If only one input was provided, calculate the other based on base conversions
        if result_metric is not None:
            final_m = METRIC_BASE_TO_M[unit_to_metric] * (result_imperial / 3.28084) 
            return {
                'value': round(final_m, 6),
                'unit_from_input': unit_to_metric,
                'converted_unit': 'm' if value_from_metric is not None else f"{unit_to_metric} to m"
            }
        elif result_imperial is not None:
             final_ft = IMPERIAL_BASE_TO_FT[unit_to_imperial] * (result_metric / 3.28084) 
             return {
                'value': round(final_ft, 6),
                'unit_from_input': unit_to_imperial,
                'converted_unit': 'ft' if value_imperial is not None else f"{unit_to_imperial} to ft"
            }

if __name__ == '__main__':
    # Sample conversions without user input
    
    converter = UnitConverter()
    
    print("Running sample unit conversion tests...")
    
    # Test 1: Meters to Feet
    result_m2ft = converter.convert_length(value_from_metric=3.5, unit_to_metric='m', value_imperial=None)
    print(f"Input: {result_m2ft['value']} meters ({result_m2ft['unit_from_input']})")
    
    # Test 2: Feet to Meters
    result_ft2m = converter.convert_length(value_imperial=10, unit_to_imperial='ft', value_from_metric=None)
    print(f"Input: {result_ft2m['value']} feet ({result_ft2m['unit_from_input']})")
    
    # Test 3: Kilometers to Feet (via meters conversion logic in class structure if applicable or direct math simulation for demo clarity)
    # Note: The specific implementation above calculates derived values. 
    # Let's demonstrate a standard KM to FT scenario by simulating the internal flow clearly via separate calls
    
    print("\n--- Additional Specific Scenarios ---")
    
    # Scenario A: 10 km -> Feet
    val_km = 10 * 3280.84 # Approximation for demo clarity in specific output if needed, 
                            # but sticking to the class logic which handles 'km' input via METRIC_BASE_TO_M
    
    result_km_ft = converter.convert_length(value_from_metric=10000, unit_to_metric='km', value_imperial=None)
    print(f"Input: {result_km_ft['value']} km ({result_km_ft['unit_from_input']})")
    
    # Scenario B: 5 inches -> Meters
    result_in_m = converter.convert_length(value_imperial=5, unit_to_imperial='in', value_from_metric=None)
    print(f"Input: {result_in_m['value']} in ({result_in_m['unit_from_input']})")