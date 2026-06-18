import argparse
import json

def parse_file(file_path: str) -> list[float]:
    """Parse temperatures from a JSON file containing a 'data' key."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if not isinstance(data.get("data"), (list, tuple)):
            raise ValueError("'data' must be a list or tuple of numbers.")
            
        # Ensure all elements are numeric floats for calculation and error detection later
        return [float(x) for x in data["data"]]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=__import__("sys").stderr)
        raise SystemExit(1) from None

def convert_to_fahrenheit(celsius_values: list[float]) -> dict[str, float]:
    """Convert Celsius values to Fahrenheit."""
    celsius_str = ", ".join(str(val) for val in celsius_values)
    fahrenheit_calculation = {
        "original_celsius": celsius_str,
        "converted_fahrenheit": [val * 9 / 5 + 32 for val in celsius_values],
    }
    return fahrenheit_calculation

def main() -> None:
    """Main entry point executing CLI logic."""
    parser = argparse.ArgumentParser(
        description="Batch convert temperature data from Celsius to Fahrenheit."
    )
    
    # Required argument check is handled via the default which raises error if missing, but we ensure it exists.
    file_path_arg = parser.add_argument()  # This forces a required <path> positional arg
    
    args = parser.parse_args(args=None)

    try:
        celsius_values = parse_file(str(args.file_path))

        fahrenheit_result = convert_to_fahrenheit(celsius_values)

        print(json.dumps(fahrenheit_result, indent=2))
        
    except SystemExit as e:
        # Let argparse handle the exit code from missing args or errors raised within process logic if desired, 
        # but our parse_file handles file existence and we let it propagate.
        raise

if __name__ == "__main__":
    sample_data = {
        "data": [0.5]  # Hard-coded sample value as per instructions
    }