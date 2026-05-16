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
    sample_hours = 15
    sample_minutes = 30
    sample_seconds = 45
    print("--- Time Unit Conversion Module ---")
    print(f"\n--- Converting from Years ---")
    seconds_from_year = convert_to_seconds(sample_years, 'year')
    print(f"{sample_years} years is approximately {seconds_from_year:.2f} seconds")
    print(f"\n--- Converting from Months ---")
    seconds_from_month = convert_to_seconds(sample_months, 'month')
    print(f"{sample_months} months is approximately {seconds_from_month:.2f} seconds")
    print(f"\n--- Converting from Days ---")
    seconds_from_day = convert_to_seconds(sample_days, 'day')
    print(f"{sample_days} days is approximately {seconds_from_day:.2f} seconds")
    print(f"\n--- Converting from Hours ---")
    seconds_from_hour = convert_to_seconds(sample_hours, 'hour')
    print(f"{sample_hours} hours is approximately {seconds_from_hour:.2f} seconds")
    print(f"\n--- Converting from Minutes ---")
    seconds_from_minute = convert_to_seconds(sample_minutes, 'minute')
    print(f"{sample_minutes} minutes is approximately {seconds_from_minute:.2f} seconds")
    print(f"\n--- Converting from Seconds ---")
    seconds_from_second = convert_to_seconds(sample_seconds, 'second')
    print(f"{sample_seconds} seconds is approximately {seconds_from_second:.2f} seconds")
    print("\n--- Converting Back from Seconds ---")
    total_seconds = convert_to_seconds(sample_years, 'year') + convert_to_seconds(sample_months, 'month') + convert_to_seconds(sample_days, 'day') + convert_to_seconds(sample_hours, 'hour') + convert_to_seconds(sample_minutes, 'minute') + convert_to_seconds(sample_seconds, 'second')
    print(f"Total calculated seconds: {total_seconds:.2f}")
    print(f"\nConverting total seconds back to Years:")
    result_years = convert_from_seconds(total_seconds, 'year')
    print(f"{total_seconds:.2f} seconds is approximately {result_years:.2f} years")
    print(f"\nConverting total seconds back to Days:")
    result_days = convert_from_seconds(total_seconds, 'day')
    print(f"{total_seconds:.2f} seconds is approximately {result_days:.2f} days")