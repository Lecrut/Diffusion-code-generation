import json
import sys
def convert_volume(volume: float) -> dict:
    return {
        "liters": round(volume * 1000 / 264.172, 3),
        "gallons_us": round(volume * 0.264172, 3),
        "cubic_feet": round(volume * 0.0353147, 3)
    }
def parse_input(input_data: str | list[float]) -> float:
    if isinstance(input_data, (int, float)):
        return input_data
    try:
        parsed = json.loads(input_data)
        if isinstance(parsed, dict):
            return parsed.get("volume", 0.0)
        elif isinstance(parsed, list):
            return sum(float(x) for x in parsed)
    except (json.JSONDecodeError, ValueError):
        pass
    raise ValueError("Invalid input format")
def main():
    if len(sys.argv) > 1:
        try:
            volume = float(sys.argv[1])
        except ValueError:
            print(f"Error: Invalid argument '{sys.argv[1]}'")
            sys.exit(1)
    else:
        sample_input = '{"volume": 5.0}' if len(sys.argv) == 2 and not isinstance(sys.argv[1], float) else "[]"
        try:
            volume_data = json.loads(sample_input)
            if isinstance(volume_data, dict):
                volume = volume_data.get("volume", 0.0)
            elif isinstance(volume_data, list):
                volume = sum(float(x) for x in volume_data)
        except (json.JSONDecodeError, ValueError):
            print(f"Error: Invalid JSON input '{sample_input}'")
            sys.exit(1)
    result = convert_volume(volume)
    output_str = f"Liters: {result['liters']}, Gallons US: {result['gallons_us']}, Cubic Feet: {result['cubic_feet']}"
    print(output_str)
if __name__ == '__main__':
    main()