import asyncio
from dataclasses import dataclass
from typing import Optional
@dataclass
class TemperatureResult:
    value: float
    unit: str
    error_message: Optional[str] = None
    def to_dict(self) -> dict:
        return {
            "value": self.value,
            "unit": self.unit,
            "error": self.error_message
        }
class TemperatureConverterService:
    VALID_UNITS = ["celsius", "fahrenheit", "kelvin"]
    @staticmethod
    def validate_input(value: float) -> bool:
        if not isinstance(value, (int, float)):
            return False
        try:
            numeric_value = float(value)
            if not isinstance(numeric_value, (int, float)):
                return False
        except ValueError:
            return False
        return True
    @staticmethod
    def validate_unit(unit: str) -> bool:
        return unit.lower() in TemperatureConverterService.VALID_UNITS
    async def convert(self, value: float, from_unit: str, to_unit: str) -> TemperatureResult:
        if not self.validate_input(value):
            return TemperatureResult(0.0, "celsius", f"Invalid numeric input: {value}")
        if not self.validate_unit(from_unit):
            return TemperatureResult(0.0, "celsius", f"Unsupported source unit: {from_unit}. Valid units are {' | '.join(TemperatureConverterService.VALID_UNITS)}")
        if not self.validate_unit(to_unit):
            return TemperatureResult(0.0, "celsius", f"Invalid target unit: {to_unit}")
        try:
            celsius = value
            from_celsius = 0.0
            if from_unit == "fahrenheit":
                from_celsius = (value - 32) * 5 / 9
            elif from_unit == "kelvin":
                from_celsius = value - 273.15
            result_value: float = 0.0
            if to_unit == "celsius":
                result_value = from_celsius
            elif to_unit == "fahrenheit":
                result_value = (from_celsius * 9 / 5) + 32
            elif to_unit == "kelvin":
                result_value = from_celsius + 273.15
            return TemperatureResult(result_value, to_unit.lower())
        except Exception as e:
            return TemperatureResult(0.0, "celsius", f"Conversion error: {str(e)}")
async def main():
    converter = TemperatureConverterService()
    test_cases = [
        {"value": 100, "from_unit": "fahrenheit", "to_unit": "celsius"},
        {"value": -40, "from_unit": "celsius", "to_unit": "fahrenheit"},
        {"value": 373.15, "from_unit": "kelvin", "to_unit": "celsius"},
        {"value": 212, "from_unit": "fahrenheit", "to_unit": "kelvin"},
    ]
    tasks = [converter.convert(tc["value"], tc["from_unit"], tc["to_unit"]) for tc in test_cases]
    results = await asyncio.gather(*tasks)
    print("Conversion Results:")
    for result, case in zip(results, test_cases):
        status = "SUCCESS" if not result.error_message else f"ERROR: {result.error_message}"
        print(f"[{case['from_unit'].capitalize()} -> {case['to_unit'].capitalize()}]")
        print(f"  Input: {case['value']}°")
        print(f"  Output: {result.value}°{result.unit}")
        if result.error_message:
            print(f"  Note: {status}")
if __name__ == '__main__':
    asyncio.run(main())