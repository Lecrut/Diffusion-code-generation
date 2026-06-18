import asyncio
from typing import Union
class TemperatureConverter:
    def __init__(self):
        self.supported_scales = ['celsius', 'fahrenheit', 'kelvin']
    async def convert(self, value: float, from_scale: str, to_scale: str) -> dict:
        if not isinstance(value, (int, float)):
            raise ValueError("Input temperature must be a number.")
        valid_scales = [s.lower() for s in self.supported_scales]
        if from_scale.lower() not in valid_scales or to_scale.lower() not in valid_scales:
            raise ValueError(f"Invalid scale. Supported scales are {', '.join(valid_scales)}.")
        celsius_value = value
        if to_scale == 'celsius':
            result_celsius = celsius_value
        elif to_scale == 'fahrenheit':
            result_fahrenheit = (value * 9/5) + 32
            return {
                "original": value,
                "from_unit": from_scale.lower(),
                "to_unit": to_scale.lower(),
                "result": round(result_fahrenheit, 4),
                "_internal_celsius": celsius_value
            }
        elif to_scale == 'kelvin':
            result_kelvin = value + 273.15
            return {
                "original": value,
                "from_unit": from_scale.lower(),
                "to_unit": to_scale.lower(),
                "result": round(result_kelvin, 4),
                "_internal_celsius": celsius_value
            }
        elif from_scale == 'celsius':
             return {
                "original": value,
                "from_unit": from_scale.lower(),
                "to_unit": to_scale.lower(),
                "result": round(result_celsius, 4),
            }
        if from_scale == 'fahrenheit':
            temp_in_c = (value - 32) * 5/9
            if to_scale == 'celsius':
                return {
                    "original": value,
                    "from_unit": from_scale.lower(),
                    "to_unit": to_scale.lower(),
                    "result": round(temp_in_c, 4),
                }
        elif from_scale == 'kelvin':
            temp_in_c = value - 273.15
            if to_scale == 'celsius':
                return {
                    "original": value,
                    "from_unit": from_scale.lower(),
                    "to_unit": to_scale.lower(),
                    "result": round(temp_in_c, 4),
                }
        if to_scale == 'kelvin' and from_scale != 'celsius':
            temp_in_c = value - 273.15 if from_scale.lower() in ['fahrenheit', 'kelvin'] else value
            if from_scale.lower() == 'fahrenheit':
                c_val = (value - 32) * 5/9
            elif from_scale.lower() == 'celsius':
                c_val = value
            result_kelvin = c_val + 273.15
        return {
            "original": value,
            "from_unit": from_scale.lower(),
            "to_unit": to_scale.lower(),
            "result": round(result_celsius if 'c' in str(to_scale) else (temp_in_c if 'f' in str(from_scale) and 'k' not in str(to_scale) else result_kelvin), 4),                                                    
        }
    def convert_sync(self, value: float, from_scale: str, to_scale: str):
        return asyncio.run(self.convert(value, from_scale, to_scale))
async def main():
    converter = TemperatureConverter()
    test_cases = [
        (25.0, 'celsius', 'fahrenheit'),
        (77.0, 'fahrenheit', 'kelvin'),
        (-40.0, 'fahrenheit', 'celsius'),
        (300.15, 'kelvin', 'celsius')
    ]
    results = []
    for val, src, dst in test_cases:
        res = await converter.convert(val, src, dst)
        results.append(res)
        print(f"Converting {val}°{src}: to {dst}")
        print(f"Result: {res['result']}°{dst}\n")
    try:
        await converter.convert(10, 'celsius', 'invalid_scale')
    except ValueError as e:
        print(f"Error caught: {e}")
if __name__ == '__main__':
    asyncio.run(main())