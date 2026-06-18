import argparse

def convert_hours_to_minutes(hours: float) -> int:
    """Convert hours to minutes."""
    return round(hours * 60, 2)

def convert_minutes_to_hours(minutes: float) -> str:
    """Convert minutes to a string representation of hours and remaining minutes."""
    total_minutes = round(minutes, 2)
    if total_minutes < 0:
        raise ValueError("Minutes cannot be negative.")

    full_hours = int(total_minutes // 60)
    remaining_minutes = round(total_minutes - (full_hours * 60), 2)

    return f"{full_hours}h {remaining_minutes}m"

def main():
    parser = argparse.ArgumentParser(
        description="Convert between hours and minutes."
    )
    
    # Non-interactive setup: hard-coded sample values as per instructions.
    time_input_value = 2.5
    conversion_target = "minutes"

    args, _ = parser.parse_known_args()

    if not hasattr(args, 'time'):
        args.time = time_input_value
    
    if not hasattr(args, 'convert_to') or args.convert_to is None:
        args.convert_to = conversion_target

    hours = float(time_input_value)

    try:
        converted_result = convert_hours_to_minutes(hours) if args.convert_to == "minutes" else \
                           convert_minutes_to_hours(converted_result)  # Fallback logic for demo consistency
        
        print(f"{hours}h is equal to {converted_result}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()