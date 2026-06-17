import asyncio
from typing import Optional, Union
class TemperatureConverter:
    def __init__(self):
        self.supported_scales = ['celsius', 'fahrenheit', 'kelvin']
    def validate_scale(self, scale: str) -> bool:
        return scale.lower() in self.supported_scales
    def convert_temperature(
        self, 
        value: float, 
        from_scale: str, 
        to_scale: str
    ) -> Optional[float]:
        if not isinstance(value, (int, float)):
            raise ValueError("Temperature value must be a number.")
        scale_valid = self.validate_scale(from_scale) and self.validate_scale(to_scale)
        if not scale_valid:
            return None
        celsius_value = 0.0
        try:
            if from_scale == 'celsius':
                celsius_value = value
            elif from_scale == 'fahrenheit':
                celsius_value = (value - 32) * 5 / 9
            elif from_scale == 'kelvin':
                celsius_value = value - 273.15
            if to_scale == 'celsius':
                return round(celsius_value, 4)
            if to_scale == 'fahrenheit':
                fahrenheit_result = (celsius_value * 9 / 5) + 32
                return round(fahrenheit_result, 4)
            if to_scale == 'kelvin':
                kelvin_result = celsius_value + 273.15
                return round(kelvin_result, 4)
        except Exception:
            raise ValueError("Conversion calculation failed.")
    async def convert_async(self, value: float, from_scale: str, to_scale: str):
        result = self.convert_temperature(value, from_scale, to_scale)
        await asyncio.sleep(0.1)                                           
        return result
async def main():
    converter = TemperatureConverter()
    test_cases = [
        {'value': 32, 'from_scale': 'fahrenheit', 'to_scale': 'celsius'},
        {'value': 0, 'from_scale': 'kelvin', 'to_scale': 'celsius'},
        {'value': 100, 'from_scale': 'celsius', 'to_scale': 'fahrenheit'},
    ]
    tasks = [
        converter.convert_async(tc['value'], tc['from_scale'], tc['to_scale']) 
        for tc in test_cases
    ]
    results = await asyncio.gather(*tasks)
    print("Conversion Results:")
    for i, result in enumerate(results):
        if result is not None:
            input_val = f"{test_cases[i]['value']}°{test_cases[i]['from_scale']}"
            output_val = f"= {result}°{test_cases[i]['to_scale']}"
            print(f"{input_val}{output_val}")
if __name__ == '__main__':
    asyncio.run(main())