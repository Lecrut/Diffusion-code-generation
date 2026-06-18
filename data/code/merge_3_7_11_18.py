class TimeConverter:
    """A class to accurately convert time between various units."""

    def __init__(self):
        pass

    @staticmethod
    def seconds_to_minutes(seconds: float) -> float:
        return seconds / 60.0

    @staticmethod
    def minutes_to_seconds(minutes: float) -> float:
        return minutes * 60.0

    @staticmethod
    def hours_to_days(hours: float) -> float:
        return hours / (24.0)

    @staticmethod
    def days_to_hours(days: float) -> float:
        return days * 24.0

    @staticmethod
    def seconds_to_hours(seconds: float) -> float:
        return seconds / 3600.0

    @staticmethod
    def hours_to_seconds(hours: float) -> float:
        return hours * 3600.0

    @staticmethod
    def minutes_to_days(minutes: float) -> float:
        return minutes / (24.0 * 60.0)

    @staticmethod
    def days_to_minutes(days: float) -> float:
        return days * (24.0 * 60.0)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    tc = TimeConverter()

    print("Time Conversion Examples:")
    
    # Seconds to Minutes and Hours
    sec_val = 7200
    min_result = tc.seconds_to_minutes(sec_val)
    hour_result = tc.seconds_to_hours(sec_val)
    print(f"{sec_val} seconds is {min_result:.1f} minutes ({hour_result}: hours)")

    # Minutes to Seconds and Days
    min_input = 360.5
    sec_output = tc.minutes_to_seconds(min_input)
    day_output = tc.minutes_to_days(min_input)
    print(f"{min_input} minutes is {sec_output:.1f} seconds ({day_output}: days)")

    # Hours to Days and Seconds
    hour_input = 48.5
    day_result = tc.hours_to_days(hour_input)
    sec_result = tc.hours_to_seconds(hour_input)
    print(f"{hour_input} hours is {day_result:.2f} days ({sec_result}: seconds)")

    # Minutes to Days and Seconds (reversed check for precision)
    min_check = 1440.5
    day_calc = tc.minutes_to_days(min_check)
    sec_back = tc.days_to_minutes(day_calc * 60 * 24)
    
    print(f"\nPrecision Check:")
    print(f"Input: {min_check} minutes")
    print(f"Converted to days: {day_calc}")
    print(f"Days back to minutes (approx): {sec_back:.1f}")

    # Edge case test with zero and negative values if applicable logic allows, 
    # though time units are typically non-negative. Here we assume standard arithmetic behavior.
    
    edge_zero = tc.seconds_to_minutes(0)
    print(f"\nEdge Case (Zero): {edge_zero} minutes")