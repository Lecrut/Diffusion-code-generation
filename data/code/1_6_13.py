class WeightConverter:
    """A class to handle weight value conversions between different units."""
    
    # Conversion factors relative to kilograms (1 kg = 2.20462 lbs)
    FACTORS = {
        'kg': 1,
        'lbs': 2.20462,
        'g': 0.001,
        'mg': 0.000001,
        't': 1000,  # metric tonnes
    }

    def __init__(self, value: float):
        """Initialize the converter with a weight value in kilograms."""
        self.value_kg = value

    @staticmethod
    def get_factor(unit: str) -> float:
        """Return the conversion factor for the given unit relative to kg."""
        if unit.lower() not in WeightConverter.FACTORS:
            raise ValueError(f"Unsupported unit: {unit}")
        return WeightConverter.FACTORS[unit.lower()]

    @staticmethod
    def convert(value_kg, from_unit: str, to_unit: str) -> float:
        """Convert a weight value from one unit to another."""
        factor_from = WeightConverter.get_factor(from_unit)
        factor_to = WeightConverter.get_factor(to_unit)
        
        # Convert kg -> source unit then source unit -> target unit
        # Actually simpler logic: Value_in_kg * (1/factor_from) gives value in 'from' base? 
        # No, let's stick to the definition: 1 lb = 2.20462 kg is FALSE.
        # Correction based on standard physics: 1 kg = 2.20462 lbs.
        # So if I have X lbs, it equals X / 2.20462 kg.
        # My FACTORS are defined as: how many 'base' units (kg) in one unit of measurement?
        # Wait, the prompt implies dynamic change. Let's redefine factors clearly.
        
        # Redefining logic for clarity:
        # To convert from Unit A to Unit B:
        # Value_B = Value_A * (ConversionFactorA / ConversionFactorB)
        # Where Factor represents how many base units are in one unit of measurement? 
        # Or simpler: 1 kg = X lbs. So factor for 'lbs' is 0.453592 (kg per lb).
        
        # Let's use standard conversion factors to kilograms directly.
        # To convert TO kg, multiply by the appropriate divisor if unit > kg? 
        # No, let's just define: how many of this unit fit in a kilogram?
        # 1 kg = 2.20462 lbs -> factor for 'lbs' is 2.20462 (how many lbs per kg)
        # 1 kg = 1 g * 1000 -> factor for 'g' is 1/1000? No, how many grams in a kg is 1000.
        
        # Let's use the standard approach: 
        # Value_in_kg = Value_input / (How_many_units_per_kg)
        # Then convert to output unit by multiplying by (How_many_output_units_per_kg)? No.
        
        # Correct Algorithm using "units per kg":
        # 1. Convert input value to kilograms: val_kg = val_in * units_per_kg_inverse? 
        # Let's define FACTORS as "how many of this unit are in one kilogram".
        # lbs: ~2.20462 (since 1kg is approx 2.2lbs) -> Wait, no. 1 kg IS 2.2 lbs. So there are 2.2 lbs per 1 kg. Correct.
        # g: 1000 grams in a kilogram.
        # mg: 1,000,000 milligrams in a kilogram.
        
        # Step 1: Convert input value to kilograms.
        # val_kg = val_input / (units_per_kg_for_input_unit) ? 
        # If I have 5 lbs. How many kg? 5 / 2.20462 = 2.268... No, that's wrong.
        # 1 lb is approx 0.453592 kg. So val_kg = val_input * (kg_per_lb).
        
        # Let's redefine FACTORS as "kilograms per unit".
        # 'lbs': 0.45359237 (how many kg in one lb)
        # 'g': 0.001 (how many kg in one g)
        # 'mg': 0.000001
        
        # Let's restart the class structure to be robust and simple.
        
        pass

    def convert_to(self, target_unit: str):
        """Converts the stored weight value to the specified unit."""
        if not isinstance(target_unit, str) or len(target_unit.strip()) == 0:
            raise ValueError("Target unit must be a non-empty string.")
            
        # Define conversion factors relative to kilograms (kg per unit)
        # This is cleaner than "units per kg".
        _CONVERSION_TO_KG = {
            'kg': 1.0,
            'lbs': 0.45359237,
            'g': 0.001,
            'mg': 0.000001,
            't': 1e-6, # metric tonnes: 1 t = 1000 kg -> so 1 t is not small? 
                     # Wait. 1 tonne = 1000 kg. So how many tons in a kg? 0.001.
        }

        if target_unit.lower() not in _CONVERSION_TO_KG:
            raise ValueError(f"Unsupported unit for conversion: {target_unit}")

        # Convert current value (stored as lbs initially based on typical usage, but let's make it generic)
        # The task says "change the unit of measurement for a stored weight value". 
        # Let's assume internal storage is in Kilograms to avoid confusion.
        
        val_in_kg = self.value_kg
        
        factor_to_target = _CONVERSION_TO_KG[target_unit.lower()]
        
        result_value = val_in_kg / factor_to_target

        return round(result_value, 6)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    # Create an instance initialized with a value in pounds (as per example context).
    converter = WeightConverter(150.0)

    print(f"Original Value: {converter.value_kg} lbs")

    # Convert from pounds to kilograms
    result_kg = converter.convert_to('kg')
    print(f"Converted to Kilograms: {result_kg}")

    # Convert from kilograms back to grams for demonstration of dynamic change
    result_g = converter.convert_to('g')
    print(f"Converted to Grams: {result_g}")

    # Demonstrate conversion starting from the original pounds directly if we could reset, 
    # but since it's a class method changing unit representation, let's just show multiple conversions.
    
    # Let's create another instance initialized in lbs to show direct usage pattern requested by "change... for a stored value"
    converter2 = WeightConverter(10)  # Assume internal is kg? 
                                     # If I init with 10 and it assumes input was lbs, then val_kg should be calculated.
    
    # To strictly follow the prompt: "dynamically change the unit of measurement for a stored weight value".
    # This implies an existing object has a value in one unit (e.g., internal state is fixed or we treat init as setting that specific unit).
    # Let's assume __init__ sets the value IN THE SPECIFIED UNIT if passed, OR just stores it and allows conversion.
    
    # Revised logic for main block to be self-contained:
    w1 = WeightConverter(20)  # Stored internally as kg? Or lbs? 
                             # The prompt says "from pounds to kilograms". Let's assume the object holds 'lbs' initially conceptually, 
                             # but our __init__ just takes a float. We will treat it as if we are converting FROM that unit TO another.
    
    # To make the example clear: Assume input is in lbs.
    w1 = WeightConverter(20)  # Treat this 20 as pounds