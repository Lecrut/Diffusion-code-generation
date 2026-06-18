import math

class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        """
        Converts length between meters (m) and feet (ft).
        
        Constants used: 
            1 meter = 3.28084 feet
        
        Args:
            value (float): The length value to convert.
            from_unit (str): Source unit ('m' for meters, 'ft' for feet).
            to_unit (str): Target unit ('m' for meters, 'ft' for feet).
            
        Returns:
            float: Converted length.
            
        Raises:
            ValueError: If unsupported units are provided or value is invalid.
        """
        
        if from_unit not in ['m', 'ft'] or to_unit not in ['m', 'ft']:
            raise ValueError("Units must be either 'm' (meters) or 'ft' (feet).")
            
        # Conversion constant: 1 meter = 3.28084 feet
        M_TO_F_FACTOR = 3.28084
        
        if from_unit == to_unit:
            return value
            
        elif from_unit == 'm':
            # Convert meters directly to target unit (either m or ft)
            # Actually, simple case: convert via common reference is not needed here 
            # We can just do direct conversion logic based on direction and units.
            
            if to_unit == 'ft':
                return value * M_TO_F_FACTOR

if __name__ == '__main__':
    pass
