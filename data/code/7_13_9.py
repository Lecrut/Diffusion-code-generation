import argparse

def convert_time(hours: int, minutes: int) -> dict[str, float]:
    """Convert hours to total minutes."""
    return {
        "hours": float(hours),
        "minutes": (float(hours) * 60.0) + float(minutes)
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert between hours and minutes.")
    
    # Since required arguments are forbidden, we provide default values for all options
    args = parser.parse_args([--hours, 25.0] + [--minutes, 30.0])

    total_minutes = convert_time(args.hours, args.minutes)
    print(f"Input: {total_minutes['hours']} hours and {total_minutes['minutes'] - int(total_minutes['hours']) * 60} minutes")
    print(f"Total Minutes: {round(total_minutes['minutes'], 2)}")