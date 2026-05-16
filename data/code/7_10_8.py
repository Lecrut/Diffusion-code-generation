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
    test_value = 7200
    test_unit = 'seconds'
    try:
        results = convert_duration(test_value, test_unit)
        print(f"Input Value: {test_value} {test_unit}")
        print("Conversion Results:")
        print(f"Seconds: {results['seconds']:.2f}")
        print(f"Minutes: {results['minutes']:.2f}")
        print(f"Hours: {results['hours']:.2f}")
        print(f"Days: {results['days']:.2f}")
        test_value = 10800
        test_unit = 'minutes'
        results = convert_duration(test_value, test_unit)
        print(f"\nInput Value: {test_value} {test_unit}")
        print("Conversion Results:")
        print(f"Seconds: {results['seconds']:.2f}")
        print(f"Minutes: {results['minutes']:.2f}")
        print(f"Hours: {results['hours']:.2f}")
        print(f"Days: {results['days']:.2f}")
        test_value = 24
        test_unit = 'days'
        results = convert_duration(test_value, test_unit)
        print(f"\nInput Value: {test_value} {test_unit}")
        print("Conversion Results:")
        print(f"Seconds: {results['seconds']:.2f}")
        print(f"Minutes: {results['minutes']:.2f}")
        print(f"Hours: {results['hours']:.2f}")
        print(f"Days: {results['days']:.2f}")
        test_value = 3600
        test_unit = 'invalid'
        print(f"\nInput Value: {test_value} {test_unit}")
        convert_duration(test_value, test_unit)
    except ValueError as e:
        print(f"\nError: {e}")