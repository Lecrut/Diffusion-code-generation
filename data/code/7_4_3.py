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
def convert_time_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    seconds = convert_to_seconds(value, from_unit)
    result = convert_from_seconds(seconds, to_unit)
    return result
if __name__ == '__main__':
    sample_years = 5
    sample_months = 60
    sample_days = 100
    sample_hours = 48
    sample_minutes = 30
    sample_seconds = 123456789
    print(f"--- Sample Conversions ---")
    print(f"\n{sample_years} Years to Days: {convert_time_units(sample_years, 'year', 'day'):.2f}")
    print(f"{sample_years} Years to Months: {convert_time_units(sample_years, 'year', 'month'):.2f}")
    print(f"{sample_years} Years to Seconds: {convert_time_units(sample_years, 'year', 'second'):.0f}")
    print(f"\n{sample_months} Months to Days: {convert_time_units(sample_months, 'month', 'day'):.2f}")
    print(f"{sample_months} Months to Hours: {convert_time_units(sample_months, 'month', 'hour'):.2f}")
    print(f"\n{sample_days} Days to Hours: {convert_time_units(sample_days, 'day', 'hour'):.2f}")
    print(f"{sample_days} Days to Minutes: {convert_time_units(sample_days, 'day', 'minute'):.2f}")
    print(f"\n{sample_hours} Hours to Minutes: {convert_time_units(sample_hours, 'hour', 'minute'):.2f}")
    print(f"{sample_hours} Hours to Seconds: {convert_time_units(sample_hours, 'hour', 'second'):.0f}")
    print(f"\n{sample_minutes} Minutes to Seconds: {convert_time_units(sample_minutes, 'minute', 'second'):.0f}")
    print(f"\n{sample_seconds} Seconds to Minutes: {convert_time_units(sample_seconds, 'second', 'minute'):.0f}")
    print(f"{sample_seconds} Seconds to Hours: {convert_time_units(sample_seconds, 'second', 'hour'):.0f}")
    print(f"{sample_seconds} Seconds to Days: {convert_time_units(sample_seconds, 'second', 'day'):.0f}")
    print(f"{sample_seconds} Seconds to Years: {convert_time_units(sample_seconds, 'second', 'year'):.2f}")
    print("\n--- Mixed Unit Test ---")
    test_value = 1
    test_unit = 'day'
    print(f"{test_value} {test_unit} to Hours: {convert_time_units(test_value, test_unit, 'hour'):.2f}")
    test_value = 7200
    test_unit = 'second'
    print(f"{test_value} {test_unit} to Minutes: {convert_time_units(test_value, test_unit, 'minute'):.2f}")