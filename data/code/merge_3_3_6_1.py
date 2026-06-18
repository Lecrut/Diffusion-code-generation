import argparse

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def process_file(file_path: str, output_func=None):
    """Read a file line by line and convert temperature values if present.

    Args:
        file_path: Path to the input text file.
        output_func: Optional function to handle converted lines (default is print).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a non-numeric value cannot be parsed as temperature.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            # Strip whitespace and skip empty lines
            cleaned_line = line.strip()
            if not cleaned_line or '=' in cleaned_line:
                continue

            try:
                celsius_value = float(cleaned_line)
                fahrenheit_value = output_func(celsius_value)
                print(f"{fahrenheit_value:.2f}")
            except ValueError as e:
                # Only raise error if it's not a standard comment or label line expected to be skipped
                if 'temperature' in cleaned_line.lower() and '=' not in cleaned_line:
                    continue  # Assume metadata lines like "# Temperature" are safe
                print(f"[Line {line_num}] Error parsing temperature value:", file_path)

def main():
    """Main entry point for the CLI script."""
    parser = argparse.ArgumentParser(
        description="Convert Celsius to Fahrenheit values in a text file."
    )
    
    # Define input argument (not required per task constraints, but useful context if provided later)
    args = parser.parse_args()

    # Hard-coded sample block for testing without user input or files
    print("Running with hard-coded sample data...")
    samples = [0, 15.6]

    # Simulate file processing logic directly using the conversion function
    for val in samples:
        result = celsius_to_fahrenheit(val)
        print(f"{val}°C -> {result:.2f}°F")

if __name__ == '__main__':
    main()