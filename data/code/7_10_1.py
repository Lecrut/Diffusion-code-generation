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
        minutes = value
        seconds = minutes * 60
        hours = minutes * 60 / 60
        days = minutes * 60 / 3600
        return {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days
        }
    elif unit == 'hours':
        hours = value
        seconds = hours * 3600
        minutes = hours * 60
        days = hours / 24
        return {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days
        }
    elif unit == 'days':
        days = value
        seconds = days * 86400
        minutes = days * 86400 / 60
        hours = days * 86400 / 3600
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
        result = convert_duration(sample_value, sample_unit)
        print(f"Input Value: {sample_value} {sample_unit}")
        print("Conversion Results:")
        print(f"Seconds: {result['seconds']:.2f}")
        print(f"Minutes: {result['minutes']:.2f}")
        print(f"Hours: {result['hours']:.2f}")
        print(f"Days: {result['days']:.2f}")
        sample_value_2 = 24 * 3600
        sample_unit_2 = 'hours'
        result_2 = convert_duration(sample_value_2, sample_unit_2)
        print("\n--- Second Sample ---")
        print(f"Input Value: {sample_value_2} {sample_unit_2}")
        print("Conversion Results:")
        print(f"Seconds: {result_2['seconds']:.2f}")
        print(f"Minutes: {result_2['minutes']:.2f}")
        print(f"Hours: {result_2['hours']:.2f}")
        print(f"Days: {result_2['days']:.2f}")
        sample_value_3 = 100800
        sample_unit_3 = 'days'
        result_3 = convert_duration(sample_value_3, sample_unit_3)
        print("\n--- Third Sample ---")
        print(f"Input Value: {sample_value_3} {sample_unit_3}")
        print("Conversion Results:")
        print(f"Seconds: {result_3['seconds']:.2f}")
        print(f"Minutes: {result_3['minutes']:.2f}")
        print(f"Hours: {result_3['hours']:.2f}")
        print(f"Days: {result_3['days']:.2f}")
        try:
            convert_duration(100, 'years')
        except ValueError as e:
            print(f"\nError Handling Test: {e}")
    except ValueError as e:
        print(f"An error occurred during conversion: {e}")