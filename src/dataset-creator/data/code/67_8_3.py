import asyncio
from typing import Union
class TemperatureConverter:
    def __init__(self):
        self.valid_scales = {'celsius', 'fahrenheit', 'kelvin'}
    async def convert(self, value: float, from_scale: str, to_scale: str) -> dict:
        if not isinstance(value, (int, float)):
            raise ValueError("Input value must be a number.")
        if from_scale.lower() not in self.valid_scales or to_scale.lower() not in self.valid_scales:
            raise ValueError(f"Invalid scale. Must be one of {self.valid_scales}.")
        celsius = None
        if from_scale == 'celsius':
            celsius = value
        elif from_scale == 'fahrenheit':
            celsius = (value - 32) * 5 / 9
        elif from_scale == 'kelvin':
            celsius = value - 273.15
        if to_scale == 'celsius':
            result = celsius
        elif to_scale == 'fahrenheit':
            result = (celsius * 9 / 5) + 32
        elif to_scale == 'kelvin':
            result = celsius + 273.15
        return {
            "input_value": value,
            "from_scale": from_scale.upper(),
            "to_scale": to_scale.upper(),
            "result": round(result, 4),
            "status": "success"
        }
async def main():
    converter = TemperatureConverter()
    test_cases = [
        {"value": 100.5, "from_scale": "celsius", "to_scale": "fahrenheit"},
        {"value": 212.0, "from_scale": "fahrenheit", "to_scale": "kelvin"},
        {"value": 373.15, "from_scale": "kelvin", "to_scale": "celsius"}
    ]
    tasks = [converter.convert(tc["value"], tc["from_scale"], tc["to_scale"]) for tc in test_cases]
    results = await asyncio.gather(*tasks)
    print("Conversion Results:")
    for result in results:
        print(f"Input: {result['input_value']} ({result['from_scale']}) -> Output: {result['result']} ({result['to_scale']})")
if __name__ == '__main__':
    asyncio.run(main())