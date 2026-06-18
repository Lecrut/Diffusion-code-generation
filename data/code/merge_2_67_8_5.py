import asyncio
from typing import Optional, Union
class TemperatureConverter:
    def __init__(self):
        self.supported_scales = ['celsius', 'fahrenheit', 'kelvin']
    def validate_scale(self, scale: str) -> bool:
        return scale.lower() in self.supported_scales
    async def convert(
        self, 
        value: float, 
        from_scale: str, 
        to_scale: Optional[str] = None
    ) -> dict:
        if not isinstance(value, (int, float)):
            raise ValueError("Temperature value must be a number.")
        scale_map = {
            'celsius': 0.0,
            'fahrenheit': -459.67,
            'kelvin': 273.15
        }
        if not self.validate_scale(from_scale):
            raise ValueError(f"Unsupported source scale: {from_scale}. Supported scales are {self.supported_scales}")
        to_scale = to_scale or from_scale
        if not self.validate_scale(to_scale) and to_scale != from_scale:
            raise ValueError(f"Unsupported target scale: {to_scale}. Supported scales are {self.supported_scales}")
        celsius_value = value - scale_map[from_scale] + 273.15
        result_celsius = celsius_value if to_scale == 'celsius' else (value * 9/5 + 32) if to_scale == 'fahrenheit' else celsius_value + 273.15
        return {
            "input": value,
            "from_scale": from_scale.upper(),
            "to_scale": to_scale.upper(),
            "result": result_celsius
        }
async def main():
    converter = TemperatureConverter()
    test_cases = [
        (0.0, 'celsius', None),
        (32.0, 'fahrenheit', 'celsius'),
        (-459.67, 'kelvin', 'celsius')
    ]
    tasks = []
    for value, from_scale, to_scale in test_cases:
        task = converter.convert(value, from_scale, to_scale)
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    print("Conversion Results:")
    for i, result in enumerate(results):
        print(f"Case {i+1}: Input={result['input']} ({result['from_scale']}) -> Output={result['result']} ({result['to_scale']})")
if __name__ == '__main__':
    asyncio.run(main())