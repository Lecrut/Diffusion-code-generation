import json
import sys
def convert_volume(volume_value: float) -> dict:
    conversions = {
        "liters": volume_value,
        "milliliters": volume_value * 1000,
        "gallons_us": round(volume_value / 3.785411784, 2),
        "quarts_us": round(volume_value / 0.946352946, 2),
        "pints_us": round(volume_value * 2.11337641, 2)
    }
    return conversions
def main():
    if len(sys.argv) > 1:
        try:
            input_volume = float(sys.argv[1])
        except ValueError:
            print("Error: Invalid volume value")
            sys.exit(1)
    else:
        sample_input = {
            "input": {"liters": 5.0},
            "output_units": ["milliliters", "gallons_us"]
        }
        input_volume = sample_input["input"]["liters"]
    result = convert_volume(input_volume)
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()