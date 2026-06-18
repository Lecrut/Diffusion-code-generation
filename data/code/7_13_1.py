import argparse

def convert_time(value: float) -> None:
    """Convert a time value between hours and minutes."""
    if isinstance(value, (int, float)):
        print(f"{value} is equivalent to {value * 60:.2f} minutes.")
    else:
        raise TypeError("Time value must be numeric.")

def main() -> None:
    """Parse command-line arguments and perform time conversion."""
    parser = argparse.ArgumentParser(
        description="Convert a time value between hours and minutes."
    )

    # Argument for the input number (hours)
    args = parser.add_argument("value", type=float, help="The number of hours to convert.")

    if len(args) == 1:
        convert_time(args.value)

if __name__ == "__main__":
    main()