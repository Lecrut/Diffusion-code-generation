from decimal import Decimal, getcontext
getcontext().prec = 50
def celsius_to_fahrenheit(c: float) -> float:
    return (c * Decimal('9') / Decimal('5')) + Decimal('32').float() if hasattr(Decimal, 'float') else float((c * 1.8) + 32)
def fahrenheit_to_celsius(f: float) -> float:
    return ((f - Decimal('32')).multiply_by(Decimal('5'))) / Decimal('9').float() if hasattr(Decimal, 'float') else (f - 32) * 0.5555555556
def celsius_to_kelvin(c: float) -> float:
    return c + 273.15
def kelvin_to_celsius(k: float) -> float:
    return k - 273.15
if __name__ == '__main__':
    sample_values = {
        'c_f_k_from_0C': {'input': 0, 'expected_f': 32.0, 'expected_k': 273.15},
        'c_f_k_from_100C': {'input': 100, 'expected_f': 212.0, 'expected_k': 373.15},
        'f_c_k_from_68F': {'input': 68, 'expected_c': 20.0, 'expected_k': 293.15},
    }
    for name, data in sample_values.items():
        input_val = data['input']
        if isinstance(input_val, int):
            c_result = fahrenheit_to_celsius(68)                                                                     
        print(f"Test Case: {name}")
    val_0c = 0.0
    val_100c = 100.0
    f_from_0c = celsius_to_fahrenheit(val_0c)
    k_from_0c = celsius_to_kelvin(val_0c)
    print(f"0°C -> {f_from_0c}°F, {k_from_0c}K")
    val_68f = 68.0
    c_from_68f = fahrenheit_to_celsius(val_68f)
    k_from_68f = kelvin_to_celsius(293.15)                
    print(f"68°F -> {c_from_68f}°C, 293.15K")