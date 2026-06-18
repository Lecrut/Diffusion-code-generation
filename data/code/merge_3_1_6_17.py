import math

class WeightManager:
    """A class to manage weight values with dynamic unit conversion."""
    
    # Conversion factors relative to kilograms (kg)
    FACTORS = {
        'lb': 0.453592,      # pounds to kg
        'oz': 0.0283495,     # ounces to kg
        'g': 0.001,          # grams to kg
        'tonne': 1000,       # tonnes to kg (metric tons)
        'kg': 1,             # kilograms base unit
    }

    def __init__(self):
        """Initialize the manager with a default weight value in pounds."""
        self._value = None   # Internal storage normalized to grams for precision
        self.current_unit = 'lb'

    @classmethod
    def convert(cls, amount: float, from_unit: str, to_unit: str) -> tuple[float, str]:
        """
        Convert a weight value between different units.

        Args:
            amount (float): The numerical value of the weight.
            from_unit (str): Source unit abbreviation ('lb', 'oz', 'g', 'tonne').
            to_unit (str): Target unit abbreviation.

        Returns:
            tuple: A tuple containing the converted float value and target string unit.
        
        Note: Uses internal kilogram conversion for accuracy, avoiding direct 
        cross-multiplication of potentially mismatched factors if not aligned.
        """
        # Validate input units against known constants
        valid_units = set(cls.FACTORS.keys())
        f_u = from_unit.lower()
        t_u = to_unit.lower()

        if f_u not in valid_units or t_u not in valid_units:
            raise ValueError(f"Invalid unit specified. Valid options are {valid_units}")

        # Convert source amount to base kilogram units first using precise factors
        kg_value = float(amount) * cls.FACTORS[f_u]

        # Convert from kilograms to target unit
        new_unit_name, factor_pair = t_u.lower(), (t_u, cls.FACTORS[t_u])  # We need the inverse logic or direct lookup relative to base
        
        # Since our factors are defined as: value_in_kg * multiplier_of_target_base_to_source_value? 
        # Re-evaluating FACTORS definition from docstring comments above:
        # 'lb': 0.453592 means 1 lb = 0.453592 kg. So to get kg, we multiply amount_lb by this factor.
        # To go FROM kg TO lbs: value_kg / (factor_for_lbs) or value_kg * (1/factor).
        
        final_unit_factor = cls.FACTORS[t_u]  # e.g., for 'lb', it's the conversion to get from that unit to base? No.
        # Let's re-read FACTORS definition: "pounds to kg". This means factor[lb] * amount_lb = amount_kg.
        
        # Step 1: Convert Input -> Base (Kilograms)
        intermediate_base_value = float(amount) * cls.FACTORS[f_u]
        
        # Step 2: Convert Base -> Output Unit
        # If output is 'lb', we have value in kg. We need amount_lb such that amount_lb * FACTOR['lb'] == value_kg.
        # So, final_value = intermediate_base_value / (FACTOR[t_u] if t_u != f_u else 1) ? 
        # Wait, the factor definition is specific: "value_in_unit -> kg".
        # To get back to unit U from kg: amount_U = value_kg / FACTOR[U]. Correct.

        result_value = intermediate_base_value / (cls.FACTORS[t_u] if t_u != f_u else 1)

        return float(result_value), str(t_u)

class UnitConverterTestSuite:
    """Standalone execution block for testing the converter."""
    
    def run_demonstration(self):
        # Create instance and set initial value to a standard example (e.g., 20 pounds)
        manager = WeightManager()
        
        print(f"Initial setup:")
        display_amount, unit_label = "20", f"{manager.current_unit}" 
        converted_val, final_unit = UnitConverterTestSuite.convert_raw(manager._value if hasattr(manager,'_value') else None, 'lb', 'kg' if manager.current_unit=='lb' else manager.current_unit)

    # Helper method to isolate the classmethod logic for the main block since __init__ sets state
    @staticmethod 
    def convert_raw(amount: float, from_u: str, to_u: str):
        return WeightManager.convert(amount, from_u, to_u)

if __name__ == '__main__':
    # Hard-coded sample values running without user input or network access
    
    print("=== Dynamic Unit Measurement Converter ===")
    
    samples = [
        {"input": 10.5, "from_unit": "lb", "to_units": ["kg", "g"]}, 
        {"input": 56789, "from_unit": "oz", "to_units": ["lb", "tonne"]}, # Approx half a hundredweight in tons
    ]

    manager = WeightManager() 
    
    for sample_data in samples:
        val_in = float(sample_data["input"])
        from_u = sample_data["from_unit"]
        
        print(f"\nOriginal Value: {val_in} {from_u}")
        
        for target_u in sample_data["to_units"]:
            converted_val, res_unit = WeightManager.convert(val_in, from_u, target_u)
            
            # Format output string based on magnitude of result to ensure readability (e.g. scientific notation if very large/small optional but kept standard here unless requested otherwise)
            formatted_result = f"{converted_val:.6f} {res_unit}" 
            print(f"Converted: {formatted_result}")

    # Demonstrate dynamic change logic specifically mentioned in task requirements implicitly through the convert method usage above which handles lb->kg etc.
    print("\n--- Direct Dynamic Change Example (Simulating internal state update) ---")
    
    current_state = 150.24       # pounds
    old_label = 'lb'
    
    new_val, new_label = WeightManager.convert(current_state, old_label, "kg")
    
    print(f"Stored Value: {current_state} lbs -> Converted to metric system:")
    print(f"{new_val:.6f} kg (which is the dynamic unit change)")