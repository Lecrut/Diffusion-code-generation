import asyncio
from typing import Union
class TemperatureConverter:
    def __init__(self):
        self.supported_scales = ['celsius', 'fahrenheit', 'kelvin']
    async def convert(self, value: float, from_scale: str, to_scale: str) -> dict:
        if not isinstance(value, (int, float)):
            raise ValueError("Input temperature must be a number.")
        valid_scales = self.supported_scales
        if from_scale.lower() not in valid_scales or to_scale.lower() not in valid_scales:
            raise ValueError(f"Invalid scale. Supported scales are {', '.join(valid_scales)}")
        celsius_value = value
        target_unit = None
        if from_scale == 'celsius':
            pass                      
        elif from_scale == 'fahrenheit':
            celsius_value = (value - 32) * 5 / 9
        elif from_scale == 'kelvin':
            celsius_value = value - 273.15
        if to_scale == 'celsius':
            return {'original_value': value, 'from_scale': from_scale, 'to_scale': to_scale, 'converted_value': round(celsius_value, 4)}
        elif to_scale == 'fahrenheit':
            fahrenheit_value = (celsius_value * 9 / 5) + 32
            return {'original_value': value, 'from_scale': from_scale, 'to_scale': to_scale, 'converted_value': round(fahrenheit_value, 4)}
        elif to_scale == 'kelvin':
            kelvin_value = celsius_value + 273.15
            return {'original_value': value, 'from_scale': from_scale, 'to_scale': to_scale, 'converted_value': round(kelvin_value, 4)}
async def main():
    converter = TemperatureConverter()
    test_cases = [
        {'value': 100.5, 'from_scale': 'celsius', 'to_scale': 'fahrenheit'},
        {'value': 212, 'from_scale': 'fahrenheit', 'to_scale': 'kelvin'},
        {'value': 373.15, 'from_scale': 'kelvin', 'to_scale': 'celsius'},
    ]
    results = []
    for case in test_cases:
        try:
            result = await converter.convert(
                value=case['value'], 
                from_scale=case['from_scale'], 
                to_scale=case['to_scale']
            )
            results.append(result)
        except Exception as e:
            print(f"Error processing {case}: {e}")
    output_data = []
    for r in results:
        output_data.append({
            "input": f"{r['original_value']}°{r['from_scale']}",
            "output": f"{r['converted_value']}°{r['to_scale']}"
        })
    print("Conversion Results:")
    for item in output_data:
        print(f"  {item['input']} -> {item['output']}")
if __name__ == '__main__':
    asyncio.run(main())