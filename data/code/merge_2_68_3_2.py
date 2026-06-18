import json
import sys
def convert_volume(value: float) -> dict:
    return {
        "liters": round(value * 1000 / 264.172, 3),
        "gallons_us": round(value / 8.798765, 3),
        "cubic_feet": round(value * 0.0353147, 3)
    }
def parse_input(input_str: str):
    try:
        data = json.loads(input_str) if input_str else {}
        return float(data.get("value", 264)) if isinstance(data, dict) and "value" in data else None
    except (json.JSONDecodeError, ValueError, TypeError):
        return None
if __name__ == '__main__':
    volume = parse_input(''.join(sys.argv[1:])) or convert_volume(50)["liters"] / 3.785412 if len(sys.argv) > 1 else 50
    result = convert_volume(volume)
    print(json.dumps(result))