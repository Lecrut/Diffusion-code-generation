import math
def convert_duration(value, unit):
    if unit == 'seconds':
        seconds = value
        minutes = seconds / 60
        hours = seconds / 3600
        days = seconds / 86400
        return {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days
        }
    elif unit == 'minutes':
        seconds = value * 60
        minutes = value
        hours = value / 60
        days = value / (60 * 24)
        return {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days
        }
    elif unit == 'hours':
        seconds = value * 3600
        minutes = value * 60
        hours = value
        days = value / 24
        return {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days
        }
    elif unit == 'days':
        seconds = value * 86400
        minutes = value * 86400 / 60
        hours = value * 24
        days = value
        return {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days
        }
    else:
        raise ValueError("Invalid unit specified. Must be 'seconds', 'minutes', 'hours', or 'days'.")
if __name__ == '__main__':
    sample_value = 7200
    sample_unit = 'seconds'
    try:
        results = convert_duration(sample_value, sample_unit)
        print(f"Input Value: {sample_value} {sample_unit}")
        print("Conversion Results:")
        print(f"Seconds: {results['seconds']:.2f}")
        print(f"Minutes: {results['minutes']:.2f}")
        print(f"Hours: {results['hours']:.2f}")
        print(f"Days: {results['days']:.2f}")
        sample_value_2 = 30
        sample_unit_2 = 'minutes'
        results_2 = convert_duration(sample_value_2, sample_unit_2)
        print("\n--- Second Sample ---")
        print(f"Input Value: {sample_value_2} {sample_unit_2}")
        print("Conversion Results:")
        print(f"Seconds: {results_2['seconds']:.2f}")
        print(f"Minutes: {results_2['minutes']:.2f}")
        print(f"Hours: {results_2['hours']:.2f}")
        print(f"Days: {results_2['days']:.2f}")
        sample_value_3 = 2
        sample_unit_3 = 'years'
        print("\n--- Error Handling Sample ---")
        convert_duration(sample_value_3, sample_unit_3)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")