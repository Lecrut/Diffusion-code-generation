import asyncio
from typing import Union
class TemperatureConverter:
    def __init__(self):
        self.supported_scales = ["celsius", "fahrenheit", "kelvin"]
    async def convert(self, value: float, from_scale: str, to_scale: str) -> dict:
        if not isinstance(value, (int, float)):
            raise ValueError("Input temperature must be a number.")
        if from_scale.lower() not in self.supported_scales or to_scale.lower() not in self.supported_scales:
            raise ValueError(f"Unsupported scale. Must be one of {self.supported_scales}")
        celsius = None
        if from_scale == "celsius":
            celsius = value
        elif from_scale == "fahrenheit":
            celsius = (value - 32) * 5 / 9
        elif from_scale == "kelvin":
            celsius = value - 273.15
        if to_scale == "celsius":
            return {"original_value": value, "from_scale": from_scale, "to_scale": to_scale, "result": round(celsius, 4)}
        elif to_scale == "fahrenheit":
            fahrenheit = celsius * 9 / 5 + 32
            return {"original_value": value, "from_scale": from_scale, "to_scale": to_scale, "result": round(fahrenheit, 4)}
        elif to_scale == "kelvin":
            kelvin = celsius + 273.15
            return {"original_value": value, "from_scale": from_scale, "to_scale": to_scale, "result": round(kelvin, 4)}
async def main():
    converter = TemperatureConverter()
    tasks = [
        asyncio.create_task(converter.convert(25.0, "celsius", "fahrenheit")),
        asyncio.create_task(converter.convert(77.0, "fahrenheit", "kelvin")),
        asyncio.create_task(converter.convert(310.15, "kelvin", "celsius")),
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(f"Converted {result['original_value']}°{result['from_scale'][:6]} to {result['to_scale']}")
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass