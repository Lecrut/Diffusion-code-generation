class VolumeConverter:
    FACTORS = {
        "liters": 1,
        "milliliters": 1000,
        "cubic_decimeters": 1.0,
        "gallons_us": 3.785411784,
        "pints_us": 2.1133764,
        "cups_us": 4.2267529,
        "ounces_us_fluid": 33.8140227,
    }
    @staticmethod
    def _validate_unit(unit: str) -> None:
        valid_units = set(VolumeConverter.FACTORS.keys())
        if not isinstance(unit, str):
            raise TypeError(f"Unit must be a string, got {type(unit).__name__}")
        if unit.lower() not in [k.lower() for k in valid_units]:
            raise ValueError(f"Unsupported volume unit: '{unit}'. Supported units are: {', '.join(valid_units)}")
    @staticmethod
    def _validate_value(value) -> None:
        try:
            numeric_val = float(value)
            if not isinstance(numeric_val, (int, float)):
                raise TypeError(f"Value must be a number, got {type(value).__name__}")
            if numeric_val < 0:
                raise ValueError("Volume cannot be negative.")
        except Exception as e:
            raise type(e)(f"Invalid value format. Error: {e}")
    @staticmethod
    def _convert_to_base(amount: float, from_unit: str) -> float:
        VolumeConverter._validate_value(amount)
        VolumeConverter._validate_unit(from_unit.lower())
        factor = VolumeConverter.FACTORS[from_unit.lower()]
        return amount * factor
    @staticmethod
    def _convert_from_base(base_amount: float, to_unit: str) -> float:
        VolumeConverter._validate_value(base_amount)
        VolumeConverter._validate_unit(to_unit.lower())
        factor = 1 / VolumeConverter.FACTORS[to_unit.lower()]
        return base_amount * factor
    @staticmethod
    def convert(amount: float, from_unit: str, to_unit: str) -> float:
        base_amount = VolumeConverter._convert_to_base(amount, from_unit)
        result = VolumeConverter._convert_from_base(base_amount, to_unit)
        return round(result, 6)
if __name__ == '__main__':
    test_cases = [
        (10.5, "liters", "gallons_us"),
        (236588.24, "milliliters", "cups_us"),
        (757.0, "ounces_us_fluid", "pints_us"),
        (1.0, "cubic_decimeters", "liters"),
    ]
    for amount_str, from_unit_str, to_unit_str in test_cases:
        try:
            result = VolumeConverter.convert(amount_str, from_unit_str, to_unit_str)
            print(f"Converted {amount_str} {from_unit_str} to {to_unit_str}: {result}")
        except Exception as e:
            print(f"Error converting {amount_str} {from_unit_str} to {to_unit_str}: {e}")
    error_tests = [
        (-5, "liters", "gallons_us"),                  
        ("invalid", "liters", "gallons_us"),                       
        (10.0, "unknown_unit", "liters"),                       
    ]
    print("\nTesting error handling:")
    for amount_str, from_unit_str, to_unit_str in error_tests:
        try:
            result = VolumeConverter.convert(amount_str, from_unit_str, to_unit_str)
            print(f"Unexpected success with {amount_str} {from_unit_str} to {to_unit_str}: {result}")
        except Exception as e:
            print(f"Expected error for {amount_str} {from_unit_str} to {to_unit_str}: {e.__class__.__name__}")
    try:
        VolumeConverter.convert("ten", "liters", "gallons_us")                            
    except Exception as e:
        print(f"Type error test result: {type(e).__name__}: {e}")