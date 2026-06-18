import json
import sys
def convert_volume(value: float) -> dict:
    return {
        "liters": round(value * 1000 / 264.172, 3),
        "gallons_us": round(value * 0.264172, 3),
        "cubic_feet": round(value * 0.0353147, 3)
    }
def parse_input(args: list[str]) -> float | None:
    if len(args) == 1 and args[0].startswith("-"):
        try:
            return json.loads(args[0])["volume"]
        except (json.JSONDecodeError, KeyError):
            pass
    for arg in args:
        try:
            val = float(arg)
            if val > 0:
                return val
        except ValueError:
            continue
    return None
if __name__ == '__main__':
    volume_input = parse_input(sys.argv[1:]) or 5.0
    result = convert_volume(volume_input)
    print(f"Input (Liters): {volume_input}")
    for unit, converted in result.items():
        print(f"{unit.capitalize()}: {converted} {unit.lower()}")