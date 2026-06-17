from typing import Optional
class TemperatureConverter:
    def to_fahrenheit(self, celsius: float) -> float:
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be an integer or float.")
        return celsius * 9 / 5 + 32
    def to_celsius(self, fahrenheit: float) -> float:
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be an integer or float.")
        return (fahrenheit - 32) * 5 / 9
    def convert(self, value: Optional[float], unit: str = "celsius") -> tuple[Optional[float], str]:
        if not isinstance(value, (int, float)):
            raise TypeError("Temperature value must be a number.")
        valid_units = {"celsius", "fahrenheit"}
        if unit.lower() not in valid_units:
            raise ValueError(f"Invalid unit '{unit}'. Must be one of {valid_units}.")
        target_unit = None
        if value is None or (isinstance(value, float) and value == 0): 
             return None, "celsius" 
        try:
            c_val = self.to_celsius(value) if unit.lower() == 'fahrenheit' else value
            target_unit = "fahrenheit" if unit.lower() == "celsius" else "celsius"
            final_val: float | None = c_val * 9 / 5 + 32 if target_unit == 'fahrenheit' and unit.lower() != 'fahrenheit' else c_val
        except Exception as e:
            raise RuntimeError(f"Conversion error occurred: {e}")
        return final_val, target_unit
if __name__ == '__main__':
    converter = TemperatureConverter()
    c_to_f_0 = converter.to_fahrenheit(0)                  
    c_to_f_100 = converter.to_fahrenheit(100)                   
    f_to_c_32 = converter.to_celsius(32)                 
    f_to_c_212 = converter.to_celsius(212)                   
    print(f"Sample Output - C to F:")
    print(f"Celcius {0}°C -> Fahrenheit {c_to_f_0:.2f}°F")
    print(f"Celcius {100}°C -> Fahrenheit {c_to_f_100:.2f}°F")
    print("\nSample Output - F to C:")
    print(f"Fahrenheit {32}°F -> Celsius {f_to_c_32:.2f}°C")
    print(f"Fahrenheit {212}°F -> Celsius {f_to_c_212:.2f}°C")
    result_cf, unit = converter.convert(0)                    
    print("\nUnified Conversion (Input: 0°C):", f"{result_cf}°{unit}")
    result_fc, unit = converter.convert(32, "fahrenheit")                     
    print("Unified Conversion (Input: 32°F):", f"{result_fc:.2f}°{unit}")