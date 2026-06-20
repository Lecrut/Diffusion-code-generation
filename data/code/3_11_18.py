import argparse
import json
import sys
from typing import List, Union

def convert_celsius_to_fahrenheit(celsius: Union[int, float]) -> float:
    return celsius * 9.0 / 5.0 + 32.0

def batch_convert_temperatures(
    input_data: List[Union[int, float]],
) -> List[float]:
    return [convert_celsius_to_fahrenheit(temp) for temp in input_data]

def load_temperature_data(file_path: str) -> List[Union[int, float]]:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Input data must be a JSON array of numbers")
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("All elements must be numeric")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in '{file_path}': {e}")

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Batch convert temperature data from Celsius to Fahrenheit."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input JSON file containing an array of Celsius temperatures.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional path to write the converted Fahrenheit values as JSON.",
    )
    return parser

def main(args=None):
    if args is None:
        args = []

    parser = create_parser()

    parsed_args = parser.parse_args(args)

    celsius_data = load_temperature_data(parsed_args.input_file)
    fahrenheit_data = batch_convert_temperatures(celsius_data)

    if parsed_args.output:
        try:
            with open(parsed_args.output, "w") as f:
                json.dump(fahrenheit_data, f)
        except IOError as e:
            raise IOError(f"Failed to write to output file '{parsed_args.output}': {e}")

    return fahrenheit_data

if __name__ == '__main__':
    import tempfile
    import os

    sample_celsius_data = [0, 100, 37, -40, 25.5]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        json.dump(sample_celsius_data, tmp)
        temp_file_path = tmp.name

    try:
        result = main([temp_file_path])
        print(result)
    finally:
        os.unlink(temp_file_path)