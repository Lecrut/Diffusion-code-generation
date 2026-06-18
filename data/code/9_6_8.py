# Volume Conversion System with Decoupled Logic Constants

class VolumeConversionFactors:
    """
    A class to store volume conversion factors using a dictionary structure.
    All logic is decoupled from the constants themselves, stored in this instance's data attribute.
    
    Attributes:
        _factors (dict): Internal storage for all defined conversion ratios relative to base unit 'liter'.
                         Key format: "{unit_to}{base_unit}" -> float ratio
    """

    def __init__(self):
        # Base unit is implicitly liters ('l'). All factors are converted TO this.
        self._factors = {}  # Type: Dict[str, float]
        
        # Define conversion constants relative to the base unit (liters)
        # Key format: "source_unit_to_base" -> value_in_liters_per_source_unit
        
        # Metric conversions
        self._add_factor("l", 1.0)          # 1 liter = 1 liter
        self._add_factor("ml", 1e-3)         # 1 ml = 0.001 liters
        self._add_factor("cl", 1e-2)         # 1 cl (centiliter) = 0.01 liters
        
        # US Customary conversions to Liters
        self._add_factor("gal_us", 3.785411784) # 1 gallon ~ 3.78 L
        self._add_factor("qt_us", 0.946352946)   # 1 quart ~ 0.946 L
        
        # Imperial/UK conversions to Liters (approx for simplicity unless specified otherwise, 
        # but standard conversion: 1 UK gallon = 4.54609 liters)
        self._add_factor("gal_uk", 4.54609)      # 1 imperial gallon ~ 4.54 L
        
    def _add_factor(self, source_unit_to_base_label: str, value_in_liters: float):
        """
        Adds a conversion factor from the specified unit to liters (base).
        
        Args:
            source_unit_to_base_label (str): Label indicating which way of mapping this constant. 
                                            Format is "{unit}{direction}", e.g., "ml_l" means ml->l, 
                                            but in our implementation we store it as a key like 'source_target' or just unique ID to avoid ambiguity?
                                            Actually, let's use a simpler approach: Key = "FROM_UNIT_TO_BASE", Value = amount_in_base_per_one_unit.
            value_in_liters (float): The volume of one unit of the source in liters.
        """
        if not isinstance(source_unit_to_base_label, str) or len(value_in_liters) == 0:
             raise TypeError("Invalid factor definition.")

    # Corrected internal implementation for cleaner keys and logic
    
class VolumeConverter(VolumeConversionFactors):
    
    def __init__(self):
        super().__init__()
        
        # Re-define factors with correct key generation based on "FROM_UNIT_TO_BASE" concept or bidirectional lookup.
        # Let's simplify: Key is "{unit}_to_base". Value is value_in_liters_per_unit_of_that_keyed_source.
        
        self._factors = {}

        # Metric
        self._set_factor("l", 1.0)          # Liter to liter ratio is 1.0 (as base reference) -> Actually better logic: 
                                             # Key: "from_l_to_base" => 1.0, but wait, usually we convert FROM X TO Y.
                                             # Let's define factors relative to Liters as the universal denominator/base for calculation ease.
        self._set_factor("l", None)         # Base unit itself
        
        # To avoid confusion with keys containing underscores or special chars in some environments:
        # We will use a simple mapping: { "source_unit": value_in_liters } 
        # And another map to convert TO liters easily. But since we need generic A -> B conversion,
        # The formula is: Val_A * (Liters_Per_1_Unit_A) / (Liters_Per_1_Unit_B).

        # Add Metric factors relative to Liters
        self._factors["liter"] = 1.0         # Amount in liters per unit of 'liter'
        self._factors["milliliter"] = 1e-3   # Amount in liters per unit of 'milliliter'
        
        # Add US Customary factors relative to Liters
        self._factors["gallon_us"] = 3.785411784 
        self._factors["quart_us"] = 0.946352946
        
        # Add UK Imperial factors relative to Liters (using standard approximations)
        self._factors["gallon_uk"] = 4.54609

    def _set_factor(self, unit: str, value_in_liters):
        """Helper to populate the internal dictionary."""
        if isinstance(unit, str) and not unit.startswith('_'):
            self._factors[unit] = float(value_in_liters)

    def convert_volume(self, amount: float, source_unit: str, target_unit: str) -> float:
        """
        Converts a volume from one unit to another using the decoupled conversion factors.
        
        Logic Flow (Decoupled):
        1. Retrieve factor for Source Unit relative to Base Liters: F_source = self._factors[source]
           If source is not found, raise ValueError.
        2. Retrieve factor for Target Unit relative to Base Liters: F_target = self._factors[target]
           If target is not found, raise ValueError.
        3. Calculate Volume in Base (Liters): Vol_liters = amount * F_source
        4. Convert from Base to Target: Result = Vol_liters / F_target
        
        Args:
            amount (float): The volume to convert.
            source_unit (str): The unit the input is currently measured in.
            target_unit (str): The desired output unit.

        Returns:
            float: Converted volume in the target unit.
            
        Raises:
            ValueError: If either source or target unit does not exist in defined factors.
        """
        
        # Validate units against available constants
        valid_units = list(self._factors.keys())
        if source_unit.lower() not in [u.lower() for u in valid_units]:
             raise ValueError(f"Unknown conversion factor: {source_unit}. Valid options: {', '.join(valid_units)}")
        
        # Normalize input keys to match internal storage (case-insensitive handling internally)
        src_key = None
        tgt_key = None
        
        if source_unit.lower() in self._factors or any(u.lower() == source_unit for u in self._factors):
            # Find the exact key matching logic. 
            # Since we just used lower case keys now, direct lookup is fine assuming consistent input format below.
             pass

        src_key = [k for k in self._factors if k.lower() == source_unit][0] if any(k.lower() == source_unit for k in self._factors) else None
        
        tgt_key = [k for k in self._factors if k.lower() == target_unit][0] if any(k.lower() == target_unit for k in self._factors) else None

        # Fallback to direct access assuming user inputs match our defined keys exactly or we normalize
        # For robustness, let's re-lookup using the normalized list
        
        def get_factor(unit_str):
            found = [k for k in self._factors if k.lower() == unit_str]
            return float(self._factors[found][0])

        f_source = get_factor(source_unit)
        
        # Check target exists before proceeding to avoid division by zero or errors
        try:
             f_target = get_factor(target_unit)
        except IndexError:
            raise ValueError(f"Unknown conversion factor: {target_unit}. Valid options: {', '.join(self._factors.keys())}")

        if not (isinstance(amount, (int, float)) and isinstance(source_unit, str)):
             raise TypeError("Amount must be numeric and units must be strings.")
             
        # Calculation logic decoupled from constants definition order or specific values
        vol_in_liters = amount * f_source
        
        return vol_in_liters / f_target

if __name__ == '__main__':
    # Sample usage block running without user input, args, or network access.
    
    converter = VolumeConverter()