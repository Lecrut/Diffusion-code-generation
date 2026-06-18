from typing import List, Union

class VolumeCalculator:
    def __init__(self):
        # Conversion factors to cubic meters (1 m^3 reference)
        self.conversions = {
            'm': 1.0,           # meter/meter cubed -> base unit is m^3, assuming input length or area? 
                              # Clarification: The task implies "volume measurements". 
                              # Standard volume units are cubic meters (m³), liters (L), gallons (gal), etc.
                              # I will assume the inputs represent volumes directly in standard units relative to a base unit of Cubic Meters (m^3).
            'cm': 1e-6,        # cm^3 = m^3 / 100^3 -> divide by 10^6? No. 
                              # Let's re-evaluate: To convert FROM input TO target base unit.
                              # If input is in "m", value is already in base (assuming m means cubic meter).
                              # Common conversions to Cubic Meter:
            'l': 0.001,       # Liter -> m^3 / 1000
            'ml': 1e-6,       # Milliliter -> m^3 / 1_000_000
            'gal_us': 0.003785412,   # US Gallon -> m^3
            'gal_imp': 0.00454609,    # Imperial Gallon -> m^3
        }

    def convert_to_base(self, value: Union[int, float], unit: str) -> float:
        """Convert a volume from the specified unit to cubic meters."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Volume must be numeric, got {type(value).__name__}")
        
        factor = self.conversions.get(unit.lower())
        if factor is None:
            raise ValueError(f"Unsupported volume unit: {unit}. Supported units are 'm', 'l', 'ml', 'gal_us', 'gal_imp'.")
        
        return value * factor

    def calculate_total_volume(self, volumes: List[Union[int, float]], target_unit: str) -> Union[float, int]:
        """
        Accept a list of volume measurements in various units and return the total 
        converted to the specified target unit.
        
        Args:
            volumes (List): A list of numeric values representing volumes. Each value must have an associated string unit.
                           Since Python lists are homogeneous, this method expects each item to be a tuple or dict 
                           containing 'value' and 'unit'. e.g., [{'val': 10, 'u': 'l'}, {'val': 5, 'u': 'gal_us'}].
            target_unit (str): The unit in which the total volume should be returned.

        Returns:
            float or int: Total volume converted to the target unit.
            
        Note: 
        To strictly follow "accept a list of volume measurements", I will assume the input format is flexible enough 
        but for type hinting and efficiency, I expect pairs (value, unit) as tuples within the list.
        If a single number is passed without context, it defaults to cubic meters ('m').

        Revised Logic based on typical "list of volumes" problems where units are often attached:
        Input format assumed: List[Tuple[float/str]] or List[Dict] -> Let's stick to Tuple (value_str_or_num, unit) 
        for clarity in type hinting. Actually, the prompt says "accept a list...". A common pattern is [val, unit].
        However, without explicit structure definition, I will assume each element is either:
        1. A number (defaulting to base 'm' if no context) - less likely for mixed units scenario unless specified per-item.
        2. OR a tuple/list of two elements [value, unit].

        Let's refine the input signature based on "various units". It is impossible to have various units in a flat list 
        without metadata. Therefore, I will assume each element is a dictionary: {'val': <number>, 'unit': '<string>'}.
        This allows for explicit type hinting and robustness against missing keys (defaulting unit to 'm').

        Actually, let's make it even simpler as per "efficient list comprehension". 
        If the input format isn't defined in the prompt specifically other than "list of volume measurements", 
        I will assume a standard tuple/list structure: [value, unit].
        
        Let's define the internal expectation clearly via type hints.
    """

    def calculate_total_volume(self, volumes: List[Union[tuple, list]], target_unit: str) -> float:
        # Normalize input to ensure every item has 'val' and 'unit'. 
        # If it's a tuple/list of 2 items, unpack them. Otherwise assume dict-like access or raise error.
        
        total_m3 = 0.0
        
        for vol in volumes:
            if isinstance(vol, (tuple, list)):
                val_str, unit_str = vol[0], str(vol[1]) 
            else: # Assume it's a number with default 'm' or raise error? 
                 # To handle "list of volume measurements" best without forcing dict syntax explicitly in prompt but implied by context.
                 # I will assume input is list of tuples (value, unit) for maximum clarity and performance.
                pass
            
            try:
                val = float(val_str) if not isinstance(vol[0], int) else vol[0] 
                # Wait, simpler type hinting: List[Tuple[float | None, str]]? No.
                # Let's assume input is exactly [float/int, string].
                
                current_unit = unit_str.lower()
            except (IndexError, TypeError):
                raise ValueError(f"Each volume measurement must be a tuple/list of format (value, unit).")

        # Efficient conversion using list comprehension and map logic manually for clarity in single module.
        
        # Re-implementing the loop with optimized structure:
        total_m3 = sum(
            self.convert_to_base(float(v[0]), str(u)) 
            if isinstance(v, (list, tuple)) else float(v) * 1.0 # Default to m^3 if not pair? No, that breaks mixed units logic.
            for v in volumes # This assumes all are tuples/lists of length >=2
        )

    def calculate_total_volume_v2(self, measurements: List[Union[tuple, list]], target_unit: str) -> float:
        """
        Optimized implementation accepting a list where each element is (value, unit).
        Converts everything to Cubic Meters and then back to Target Unit.
        
        Args:
            measurements (List[Tuple[float | int, str]]): List of tuples containing numeric value and string unit.
            target_unit (str): The desired output unit.

        Returns:
            float: Total volume in the specified unit.
        """
        # 1. Convert all inputs to Cubic Meters efficiently
        total_m3 = sum(
            self.convert_to_base(float(v[0]), str(u)) 
            for v, u in measurements if isinstance(v, (list, tuple)) and len(v) >= 2
        )

        # Handle edge case where target_unit might not be in conversion dict directly but is base 'm' or similar?
        # We need a reverse lookup to convert m^3 back to target.
        
        def get_factor_to(target: str, source_m3_val: float) -> Union[float, int]:
            if target.lower() == 'm': return source_m3_val
            
            # Inverse conversion factors (Target / Base) = Factor * Target_Value 
            # Value_Target = Source_Meters^3 / Conversion_To_Base(Target)? No.
            # We have: Volume_in_Unit_X = X_Factor * m3
            # So, 1 Unit_X = X_Factor m3 -> To get Vol in Units from m3: Val_m3 * (1/X_Factor) ? 
            # Let's check logic:
            # If I have 10 liters. Factor(liters_to_m3) = 0.001. Total_M3 = 10 * 0.001 = 0.01. Correct.
            # Now convert to Liters from Meters^3? 
            # Vol_Liters = Vol_M3 / Factor(liters_to_m3) -> 0.01 / 0.001 = 10. Correct.

if __name__ == '__main__':
    pass
