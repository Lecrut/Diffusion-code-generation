import math
def convert_to_seconds(value, unit):
    if unit == 'year':
        return value * 365.25 * 24 * 60 * 60
    elif unit == 'month':
        return value * 30.44 * 24 * 60 * 60
    elif unit == 'day':
        return value * 24 * 60 * 60
    elif unit == 'hour':
        return value * 60 * 60
    elif unit == 'minute':
        return value * 60
    elif unit == 'second':
        return value
    else:
        raise ValueError("Invalid unit specified")
def convert_from_seconds(seconds, unit):
    if unit == 'year':
        return seconds / (365.25 * 24 * 60 * 60)
    elif unit == 'month':
        return seconds / (30.44 * 24 * 60 * 60)
    elif unit == 'day':
        return seconds / (24 * 60 * 60)
    elif unit == 'hour':
        return seconds / (60 * 60)
    elif unit == 'minute':
        return seconds / 60
    elif unit == 'second':
        return seconds
    else:
        raise ValueError("Invalid unit specified")
if __name__ == '__main__':
    sample_years = 2
    sample_months = 6
    sample_days = 10
    sample_hours = 14
    sample_minutes = 30
    sample_seconds = 5
    print("--- Time Unit Conversion Module ---")
    print(f"\nSample Input:")
    print(f"Years: {sample_years}")
    print(f"Months: {sample_months}")
    print(f"Days: {sample_days}")
    print(f"Hours: {sample_hours}")
    print(f"Minutes: {sample_minutes}")
    print(f"Seconds: {sample_seconds}")
    total_seconds_from_years = convert_to_seconds(sample_years, 'year')
    print(f"\nConversion Check (Years to Seconds):")
    print(f"{sample_years} years is approximately {total_seconds_from_years:.2f} seconds.")
    total_seconds_from_months = convert_to_seconds(sample_months, 'month')
    print(f"Conversion Check (Months to Seconds):")
    print(f"{sample_months} months is approximately {total_seconds_from_months:.2f} seconds.")
    total_seconds_from_days = convert_to_seconds(sample_days, 'day')
    print(f"Conversion Check (Days to Seconds):")
    print(f"{sample_days} days is approximately {total_seconds_from_days:.2f} seconds.")
    total_seconds_from_hours = convert_to_seconds(sample_hours, 'hour')
    print(f"Conversion Check (Hours to Seconds):")
    print(f"{sample_hours} hours is approximately {total_seconds_from_hours:.2f} seconds.")
    total_seconds_from_minutes = convert_to_seconds(sample_minutes, 'minute')
    print(f"Conversion Check (Minutes to Seconds):")
    print(f"{sample_minutes} minutes is approximately {total_seconds_from_minutes:.2f} seconds.")
    print(f"Conversion Check (Seconds to Seconds):")
    print(f"{sample_seconds} seconds is {sample_seconds:.2f} seconds.")
    seconds_from_years = convert_from_seconds(total_seconds_from_years, 'year')
    print(f"\nConversion Check (Back to Years):")
    print(f"{total_seconds_from_years:.2f} seconds is approximately {seconds_from_years:.2f} years.")
    seconds_from_months = convert_from_seconds(total_seconds_from_months, 'month')
    print(f"Conversion Check (Back to Months):")
    print(f"{total_seconds_from_months:.2f} seconds is approximately {seconds_from_months:.2f} months.")
    seconds_from_days = convert_from_seconds(total_seconds_from_days, 'day')
    print(f"Conversion Check (Back to Days):")
    print(f"{total_seconds_from_days:.2f} seconds is approximately {seconds_from_days:.2f} days.")
    seconds_from_hours = convert_from_seconds(total_seconds_from_hours, 'hour')
    print(f"Conversion Check (Back to Hours):")
    print(f"{total_seconds_from_hours:.2f} seconds is approximately {seconds_from_hours:.2f} hours.")
    seconds_from_minutes = convert_from_seconds(total_seconds_from_minutes, 'minute')
    print(f"Conversion Check (Back to Minutes):")
    print(f"{total_seconds_from_minutes:.2f} seconds is approximately {seconds_from_minutes:.2f} minutes.")
    seconds_from_seconds = convert_from_seconds(sample_seconds, 'second')
    print(f"Conversion Check (Back to Seconds):")
    print(f"{sample_seconds:.2f} seconds is {seconds_from_seconds:.2f} seconds.")